# Secret of the Polyglot
### Author : SYREAL

## Description
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/97/flag2of2-final.pdf).

## Solution
Since i check the **pdf** file, it seems like it's corrupted file.  So, i decided to check what kind of filetype is it. try `file flag2of2-final.pdf`
![image](https://github.com/user-attachments/assets/69c54de8-9819-40f6-9d6d-03ae544dfd23)
Oh, so it's a png file. Then just rename the extension of the file from **pdf** to **png**. Boom! you got the real flag!!

![flag2of2-final](https://github.com/user-attachments/assets/4482fc3e-4b9a-41dd-96c4-fb8823a4b728)

## Flag
<details>
  <summary>This is the flag</summary>

  ```
  picoCTF{f1u3n7_}
  ```
</details>


<p>&copy; abiabdillahx</p>
