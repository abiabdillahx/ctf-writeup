### Author: Michael Crotty

## Description
This service provides you an encrypted flag. Can you decrypt it with just N & e?Connect to the program with netcat:`$ nc verbal-sleep.picoctf.net 51624`The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/2fa54d419e929397792d7873f14bdf16c13a80934729169464f967868e8235ac/encrypt.py).

## Solution
Ok. so, this challenge source use a RSA system to encrypt the flag we need. We already have the m, N, and c when we conect to the server with **netcat**.
![[rsa-netcat.png]]
Ok, we can actually find the `p` and `q` from N with [factordb.com](factordb.com)
![[factorize.png]]
So, the p and q was found
Then, just use this formula to decrypt it and make the script with python.
<img text-align=center src=img/rsa.png>

```python
from Crypto.Util.number import inverse, long_to_bytes

# known
e = 65537
ciphertext = 16264593387290010768272976855867140977799262321712528186766717352788799914153636185370004277544787447794929421304358995947809666963905581712452754903721441
N = 20493578506605622760176548334899367832567010456606169050310281135862599599644885076097511417550113584866678011785910020757761116878175166198173512584107078

# factor from N
p = 10246789253302811380088274167449683916283505228303084525155140567931299799822442538048755708775056792433339005892955010378880558439087583099086756292053539
q = 2

# calc φ(N) = (p-1) * (q-1)
phi_N = (p - 1) * (q - 1)

# Hitung d (private key)
d = inverse(e, phi_N)

# decrypt
m = pow(ciphertext, d, N)

# Konversi ke string
flag = long_to_bytes(m).decode(errors="ignore")
print(flag)

```
 Once u run this script, it will print the flag out

## Flag
<details>
  <summary>This is the flag</summary>

  ```
  picoCTF{tw0_1$_pr!m378257f39}
  ```
</details>
<br><br>
<p>&copy abiabdillahx</p>

