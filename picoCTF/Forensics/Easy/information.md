# information
### Author: Susie

## Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg).

## Solution
Setelah kita mengunduh file gambar yang diberikan, kita mendapatkan sebuah gambar kucing yang duduk di depan komputer(?!!).
Terus diapain?!! saya sudah mencoba scan gambar ini di **Google Lens**, tetapi tidak mendapatkan apa-apa.
</br>
Setelah berpikir sebentar, sepertinya flag dari challenge ini ada di dalam _metadata_ dari gambar kucing ini.
> **Metadata**
> adalah informasi terstruktur yang mendeskripsikan, menjelaskan, menemukan, atau setidaknya menjadikan suatu informasi mudah untuk ditemukan kembali, digunakan, atau dikelola. Metadata sering disebut sebagai data tentang data atau informasi tentang informasi. Wikipedia

Langsung saja kita gunakan **exif tools** yang ada di internet. Disini, saya menggunakan [exif.tools](https://exif.tools). Kita upload file gambar yang telah kita download tadi.
![image](https://github.com/user-attachments/assets/8563e775-56c9-46ca-b77d-52c3a504552a)</br>

Nah, setelah di-upload, langsung saja kita lihat rincian **metadata** yang ada pada file **cat.jpg**. 
![image](https://github.com/user-attachments/assets/ddfa3cdc-6bf8-4602-909a-7c5f12ef93bd)
</br>

Sepertinya, terdapat sebuah string di bagian "license" yang dienkripsi dengan sistem **Base64**. Saya coba decrypt dengan command line di bawah.
![image](https://github.com/user-attachments/assets/ad9cb4ec-ecff-4f39-8f9f-fb5fa8b60fd2)

</br>
Yeahhh!! kita dapat flagnya

## Flag
<details>
  <summary>Ini Flag-nya pak</summary>
  
  ```
  picoCTF{the_m3tadata_1s_modified}
  ```
</details>

<p>&copy abiabdillahx</p>


