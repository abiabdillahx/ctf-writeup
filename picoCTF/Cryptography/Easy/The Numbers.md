# The Numbers
### Author: Danny

## Description
**The [numbers...](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png) what do they mean?**

## Solution 
Pada challenge kali ini, kita diberikan sebuah gambar yang berisi angka-angka seperti ini.
![the_numbers](https://github.com/user-attachments/assets/b345e8db-09b5-4550-93db-f27838c51c5c)
</br></br>
Hal ini jelas menunjukkan bahwa flag yang kita cari dienkripsi menjadi deretan angka. Setelah mencari tahu beberapa teori, sepertinya sistem enkripsi yang sesuai adalah **A1Z26**. 
Enkripsi ini sesuai namanya, huruf A adalah angka 1 dan Z adalah 26. Kita dapat memecahkan kode ini dengan manual tapi ribet. Agar lebih efisien, saya menggunakan tool [A1Z26 Cipher](https://cryptii.com/pipes/a1z26-cipher) dari __*cryptii*__.
</br>
Saya memasukkan angka-angka yang ada dalam gambar itu satu per satu
```
16 9 3 15 3 20 6 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14
```

![image](https://github.com/user-attachments/assets/4452ff8f-786e-478e-bc3f-1bda49c8db97)

### Boom! kita mendapatkan sebuah kata `picoctfthenumbersmason`
> Seperti yang kita ketahui, kita harus submit flag dengan format `picoCTF{}`
Maka dari itu, dari kata yang telah didecrypt, kita abaikan **picoctf**nya. </br>

Selanjutnya, kita submit `thenumbersmason` ke dalam format flag.

![image](https://github.com/user-attachments/assets/3f7b70ed-83c9-4aff-9235-bd3f0eacde83)

## Flag
<details>
  <summary>Ini flag-nya</summary>

  ```
    picoCTF{thenumbersmason}
  ```
</details>
<p>&copy abiabdillahx</p>
