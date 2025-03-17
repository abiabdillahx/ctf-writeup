# K!nd4SUS CTF 2025
CTFTime: https://ctftime.org/event/2703

## Misc
### Otamatone my beloved
**Description**

> I was studying how to play the Otamatone when a stranger stole my pc. I wonder if he did anything strange with it...
>
> download files at https://drive.google.com/file/d/1fVNWqYGt-4-zChfzo3wW9MyK5Zn765kJ/view?usp=drive_link


**Solve**

Ok, actually, what i did for this chall is unzip the file (`otamatone.zip`). It has a `dump.raw`. It's an uncompressed image data. Then , i just check any CLI forensic tool one by one. I tried exiftool, steghide, binwalk, and finally got the flag using `strings` command. It's because we already know the flag is in KSUS{*} format. It will take a bit time because its size is 3.2 GB.
![Screenshot 2025-03-18 051929](https://github.com/user-attachments/assets/cff97e16-e386-468c-b713-5a7e21dd78ab)


**Flag**
```
KSUS{d0_I_n33d_4n_MSc_t0_us3_v0la7ili7y?_dhx8z}
```


## OSINT
### Hop on, hop off #1
**Description**

> Enjoying brunch. Flag format: KSUS{Name_Of_Brunch_Spot}
> Attachment : [1.png](./1.png)

**Solve**

What i did forstly is put this picture to **Google Lens**. Actually we can see that it is accross a restaurant named "Panda wok" in Budapest. After taht, move to Google Maps to see what is actually accross the restaurant. 
![Screenshot 2025-03-18 043629](https://github.com/user-attachments/assets/de59cdc3-7d70-43b5-99a8-365e2373503d)


We all see there is a brunch cafe named **"Cafe Muse"**. Just wrap it to KSUS{} format and challenge solved!

**Flag**
```
KSUS{Cafe_Muse}
```

## Rev-Pwn
### Granny's gift
**Description**

> My sweet Italian grandma made this beautiful keychain for me... She keeps saying it's just a keychain, but I really don't believe her!
> Attachment : [challenge.zip](./challenge.zip)


**Solve**

Ok, firstly, we gotta open the zip file up. After i opened it, it has 2 files (`whatisthis.py` adn `gift.png`). The `whatisthis.py` is a python script that has the flag we need. If you look at it more closely, you can see that it's a simple script that prints out the flag if we know the **key**. 
[ss gambar]

It looks like hash with md5 or sha256. So, i used [online tool](https://crackstation.net/) or click this https://crackstation.net/ for cracking this hash. I got "ti amo" as the key. Run the python script, then input the key, Boomm!!
![Screenshot 2025-03-18 041805](https://github.com/user-attachments/assets/10d0ccb3-40ee-4200-945e-3bf3f215a17f)

**Flag :**
```
KSUS{W3_us3d_t0_s3nd_th3s3_w1th_p1g30ns_4t_my_t1m3_y0u_kn0w}
```


========================================================


Thanks for read this writeup. If u wanna support me, buy me a coffee [here](https://ko-fi.com/abiabdillah) or click button below

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/abiabdillah) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/abiabdillahx)
