# WolvCTF 2025
CTFTime : https://ctftime.org/event/2579
Date : 22 March, 06:00 UTC+7 — 24 March 2025, 06:00 UTC+7

> [!IMPORTANT]  
> I made the **Beginner** category writeups separated from others, check it out > [Beginner Category](./Beginner.md)

<details>
    <summary>Table of Contents</summary>

1. [Misc](#-misc)
    - [Eval is Evil](#eval-is-evil)
2. [Forensics](#️️-forensics)
    - [Passwords](#passwords)
    - [Breakout](#breakout)
3. [Web Exploitation](#-web-exploitation)
    - [Javascript Puzzle](#javascript-puzzle)
</details>

# ✨ Misc
## Eval is Evil
### Description
> If eval is so bad, then why is it so easy to use?
`nc evalisevil.kctf-453514-codelab.kctf.cloud 1337`

**Attachment file** : [chall.py](./files/chall.py)

### Solve
I connect to netcat connection first, and got a unsolvable question (who tf can guess a number in range of 0 and 18446744073709551616?!). Ok, after analyze the **chall.py** script, i understand that this challenge used "eval()" function as input from users. This is a vulnerability. It's not just a simple input validation, it's a code injection. So, i can use this to execute any python code from input form.

Because the flag is in same directory as the chall.py, I tried to input this code:
```python
__import__('os').system('cat flag.txt')
```

Boom!, I got the flag
[gambar ss]


**Flag :**
```flag
wctf{Why_Gu3ss_Wh3n_Y0u_C4n_CH34T}
```

# 🕵️‍♂️ Forensics
## Passwords
### Description
> I heard you're a hacker. Can you help me get my passwords back?

**Attachment file:** [Database.kdbx](./files/Database.kdbx)

### Solve
Yea, it's a password database file. It can contains username, password, email, etc. Si, what should i do forst is try to open it using [Keepass](https://keepass.info/). And it requires a master password that i don't even know what it is. So, i have to crack it with **JohnTheRipper** and rockyou.txt.
```sh
keepass2john Database.kdbx > sec.hash
john --wordlist=/usr/share/wordlists/rockyou.txt sec.hash
john --show sec.hash
```
[gambarss]


Just explore the database and right click on the mouse to copy the password (don't forget to paste it immediately because it will be cleared after that). After i explored it, i got the real flag in "**Homebanking**" password.
Yohoooo!

**Flag :**
```flag
wctf{1_th0ught_1t_w4s_s3cur3?}
```

## Breakout
### Description
> Something fishy about that photo... What could be hidden in this game?

**Attachment file :** [breakout.jpg](./files/breakout.jpg)

### Solve
After analyze the image, I found a hidden file inside the image. I used steghide to extract it. It will extracted a **ch8** file. Ok, actually i have no idea what kind of file it is.
[gambar ss]

After minutes of searching for references, i finally knew that it's a Chip-8 ROM file that built for simple game emulator. I just found about web that can run it, [Octo](https://johnearnest.github.io/Octo/). Click 'Open' to open the breakout.ch8 file then run it. Yea, u have to win to get the flag.
[gambar ss]


**Flag :**
```flag
WCTF{GAME_OVER_VMASBKLTNUFMGS}
```


# 🌐 Web Exploitation
## Javascript Puzzle
### Description
> It is often useful to force exceptions to potentially get back valuable information.
>Can you make a request which causes an exception in this app?
>
> https://js-puzzle-974780027560.us-east5.run.app

**Attachment file :** [dist.tar.gz](./files/dist-js.tar.gz)

### Solve
So, i have a js server code written in **express.js**. Let's analyze it! When i access the website, it just shows "Hello Guest". Then, after read the **_app.js_** from attachment file, i found something interesting. There is a try-catch system that will shows the message that i saw first. So, this is what i got :
- If i access the web without any username, it'll shows "Hello Guest"
- If i access it with "**?username**=" parameter, it'll shows "Hello *username*"
- If server get any error, it will open flag.txt file
[gambar ss]

Ok then. I have to bypass the ?username parameter and make an error. Just try add this `?username[toString]=null` to the url and it'll shows the flag.txt file. 

> [!TIP]
> WHy is this happen?
> Because `toString()` method is called when we try to concatenate a string with a null value. So, it'll make an internal server error that bring us to the flag.


**Flag :**
```flag
wctf{3xc3pt10n5_4r3_y0ur_fr13nd_14285137553}
```