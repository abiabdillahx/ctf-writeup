# THJCC CTF 2024


# Crypto

## girlfriend
**Description**
> Kohiro拿到了一段女友給的密文，但是他不知道這是什麼請幫她解密 Kohiro received a mysterious encoded message from his girlfriend, but he doesn't know what it is. Please help him decode it. WkdsWmIwbFRSazFaUkVKTFdIcHdhazFFTVdaa01EUTk=

**Solve**
So, this challenge doesn't provide any file attachment or something else. Then, i know this is a classical cipher that we can solve from any online tools. For a quick solve, i used [CyberChef](https://gchq.github.io/CyberChef/). </br>
Firstly, i tried to use Base64 to decode it because it's identically similiar with Base64 format. But it is still encrypted. I tried Base64 again and again until 3 times. After that, the encrypted format looks like ROT47.
![Screenshot 2025-01-05 130805](https://github.com/user-attachments/assets/aef8b919-ce86-442a-bfb3-fb7ef8eb10a1)

```flag
THJCC{1_l0v4_y0U}
```

## S-box
**Description**
> In cryptography, an S-box (substitution-box) is a basic component of symmetric key algorithms which performs substitution. In block ciphers, they are typically used to obscure the relationship between the key and the ciphertext, thus ensuring Shannon's property of confusion. Mathematically, an S-box is a nonlinear vectorial Boolean function.

**Solve**
In this challenge, author provided 2 attachment files, `chal.py` and `output.txt`. The `output.txt` is the encrypted flag, and the `chal.py`is the encrypting system used for output.

It's an S-box encryption system. Then, i search in google and found the exact paragraph as the description does.
> In cryptography, an S-box (substitution-box) is a basic component of symmetric key algorithms which performs substitution. In block ciphers, they are typically used to obscure the relationship between the key and the ciphertext, thus ensuring Shannon's property of confusion. Mathematically, an S-box is a nonlinear[1] vectorial Boolean function.[2] (Wikipedia)

So, just make a script to reverse the S-box, then decode the Base64 cipher text. Here is my scrip
```python
import base64

# Output
cipher_hex = "b16e45b3d1042f9ae36a0033edfc966e00202f7f6a04e3f5aa7fbec7fc23b17f6a04c75033d12727"
cipher_bytes = bytes.fromhex(cipher_hex)

# Sbox from chal.py
Sbox = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

# Reverse Sbox
inverse_Sbox = {v: k for k, v in enumerate(Sbox)}

# Decrypt cipher_bytes
decrypted_bytes = bytes(inverse_Sbox[b] for b in cipher_bytes)

# Decode the base64
decoded_flag = base64.b64decode(decrypted_bytes).decode('utf-8')
decoded_flag

```
Once u run it, u will find the plaintext (flag).
```flag
THJCC{1t_INDE3d_C0nFuSed_Me}
```

# Web

## notepad
**Description**
> 

**Solve**
![image](https://github.com/user-attachments/assets/9fb74e58-4c39-45d9-a439-2bc3aa5ae92e)
![image](https://github.com/user-attachments/assets/cf4aeaad-991e-43a9-89de-5692d4710bc3)

So, index.htmlis in the /template  folder and flag.txt is in the main folder. If i want to access the flag.txt, i have to change the cookies value of the web that i accessing.

![Screenshot 2025-01-09 104033](https://github.com/user-attachments/assets/f4beb959-5c84-4fdd-82f4-1ed77978b42b)

![Screenshot 2025-01-05 130455](https://github.com/user-attachments/assets/3b2cf63b-5348-46e6-aaf0-9dd7784f0e3e)

Yeah, we got the real flag from changing a value of cookie session 




```flag
THJCC{tmp_1n_🐍_01b4c87cabcca82b}
```




========================================================


Thanks for read this writeup. If u wanna support me, buy me a coffee [here](https://ko-fi.com/abiabdillah) or click button below

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/abiabdillah) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/abiabdillah)
