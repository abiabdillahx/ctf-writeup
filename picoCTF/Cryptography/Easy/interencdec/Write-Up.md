# interencdec
### Author: NGIRIMANA Schadrack

## Description
Can you get the real meaning from this file.</br>
Download the file [here.](https://artifacts.picoctf.net/c_titan/108/enc_flag)

## Solution
1. Setelah kita mengunduh file yang diberikan, kita dapat membukanya dengan **Notepad** biasa. Akan terlihat kode seperti ini. </br></br>
![enc_file](Notepad.png)
</br>
2. Dari yang terlihat, kode ini dienkripsi menggunakan enksripsi **Base64**. Langsung saja kita gunakan tool **Base64 Decoder** dari website [cryptii](https://cryptii.com/pipes/caesar-cipher).
Setelah itu, masukkan kode yang ada di file tadi.</br></br>
![image](https://github.com/user-attachments/assets/34cb0897-8b59-4e1e-8525-226616c6e77d)
</br>
4. Kelihatannya, output yang didapat masih dalam bentuk **base64**. Tapi, kita abaikan huruf di luar tanda `''`. Sehingga, kita akan mendekripsi kode `d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==`. </br></br>
![image](https://github.com/user-attachments/assets/e78febce-fa66-41b6-aa4f-faaad4d97838)
</br>
5. Wow, kode yang dihasilkan sudah memiliki format `xxx{flag}`. Sepertinya kita sudah dekat dengan flag. 
![Screenshot 2024-10-27 003329](https://github.com/user-attachments/assets/0d226ed8-b370-49dc-ad79-3d4912cc47e2)

