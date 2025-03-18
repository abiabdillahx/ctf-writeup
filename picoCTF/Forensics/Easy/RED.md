# RED
### Author: Shuailin Pan (LeConjuror)

## Description
RED, RED, RED, RED
Download the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)

## Solution
Okay, i got an image. So what i did first is check the metadata of this image using `exiftool` command. We can see here, there is "Poem" down there. If the first letter of the sentences combined, we will get a hint. **CHECK THE LSB.**

![Screenshot 2025-03-19 044542](https://github.com/user-attachments/assets/ce606a16-20b6-43e4-ab38-e6d06b424fe2)


So, if it is an LSB steganography method, i used `zsteg` command to check it. After that, i got a **Base64 encoded** message. And if we decode it, we will get the flag. 

![Screenshot 2025-03-19 044557](https://github.com/user-attachments/assets/b140097b-ab1d-48c1-845f-590f8f16d1b9)

Here's the flag

## Flag
<details>
  <summary>This is the flag</summary>

  ```
  picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
  ```
</details>

</br></br>
<p>by abiabdillahx</p>
