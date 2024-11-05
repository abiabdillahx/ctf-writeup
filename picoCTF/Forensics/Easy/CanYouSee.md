# CanYouSee
### Author : Mubarak Mikail

## Description
How about some hide and seek?
Download this file [here.](https://artifacts.picoctf.net/c_titan/130/unknown.zip)

## Solution
Kita telah mengunduh zip archive file yang diberikan oleh picoCTF. Kemudian, kita extract file-nya untuk mendapat sebuah gambar tanpa konteks. Setelah saya buka dengan exiftool (anda bisa menggunakan tools online ataucommand line di kali linux), kita mendapatkan sebuah string yang berbentuk base64 encrypt pada bagian "Atribution URL". 
![image](https://github.com/user-attachments/assets/36962e41-0b7c-434c-9a6c-1ed6486bb209)</br></br>
Saya coba untuk decode dengan command berikut
```echo cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg== | base64 -d```
Langsung terlihat flag dari encrypted string tersebut

## Flag
<details>
  <summary>Ini yahh flag-nya</summary>

  ```
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
  ```
</details>

<p>%copy abiabdillahx</p>
