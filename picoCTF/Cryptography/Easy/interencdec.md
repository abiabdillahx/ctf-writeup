# interencdec
### Author: NGIRIMANA Schadrack

## Description
Can you get the real meaning from this file.</br>
Download the file [here.](https://artifacts.picoctf.net/c_titan/108/enc_flag)

## Solution
1. Setelah kita mengunduh file yang diberikan, kita dapat membukanya dengan **Notepad** biasa. Akan terlihat kode seperti ini. </br></br>
![enc_file](img/Notepad.png)
</br>

2. Dari yang terlihat, kode ini dienkripsi menggunakan enksripsi **Base64**. Langsung saja kita gunakan tool **Base64 Decoder** dari website [cryptii](https://cryptii.com/pipes/text-to-base64).
Setelah itu, masukkan kode yang ada di file tadi.
![Step1](https://github.com/user-attachments/assets/34cb0897-8b59-4e1e-8525-226616c6e77d)
</br>

4. Kelihatannya, output yang didapat masih dalam bentuk **base64**. Tapi, kita abaikan huruf di luar tanda `''`. Sehingga, kita akan mendekripsi kode `d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==`. 
![Step2](https://github.com/user-attachments/assets/e78febce-fa66-41b6-aa4f-faaad4d97838)
</br>

5. Wow, kode yang dihasilkan sudah memiliki format `xxx{flag}`. Sepertinya kita sudah dekat dengan flag. Tapi, bentuk enkripsi apakah ini? `wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}`
![Step3](https://github.com/user-attachments/assets/0d226ed8-b370-49dc-ad79-3d4912cc47e2)
</br>

6. Setelah melihat beberapa referensi atau mencoba [decode identifier](https://www.dcode.fr/cipher-identifier), sepertinya kode yang didapat merupakan Caesar cipher. Enkripsi ini memungkinkan seseorang menggeser alfabet tertentu sebanyak n kali sesuai dengan kunci. Pada kesempatan kali ini, saya menggunakan tool dari [cryptii](https://cryptii.com/pipes/caesar-cipher) juga.
![Step4](https://github.com/user-attachments/assets/2da9c325-6eea-4212-92f0-a77be8dbae5a)
</br>

### Boomm! kita dapat flag-nya

## Flag
<details>
  <summary>Ini flag-nya</summary>

  ```
  picoCTF{caesar_d3cr9pt3d_a47c6d69}
  ```
</details>

</br></br>
<p>&copy abiabdillahx</p>



