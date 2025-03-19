# hashcrack
### Author: Nana Ama Atombo-Sackey

## Description
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
Access the server using `nc verbal-sleep.picoctf.net 52014`

## Solution
This is a simple hash cracking challenge. I got a reference about hash theory from here :
- https://en.wikipedia.org/wiki/MD5
- https://en.wikipedia.org/wiki/SHA-1
- https://en.wikipedia.org/wiki/SHA-2

So, when i start the netcat connection, it will show me the hash of the password. I will then use a hash cracker to crack the hash ([Online tools](https://crackstation.net/)). It helped me to get the password. The server needs 3 passwords to access the flag. It is MD5, SHA-1, and SHA-256. After cracks all the password, i got the flag.

![Screenshot 2025-03-19 042343](https://github.com/user-attachments/assets/84c70390-773d-446d-ab86-1155b25886a1)



## Flag
<details>
  <summary>This is the flag</summary>

  ```
  picoCTF{UseStr0nG_h@shEs_&PaSswDs!_7f29c9da}
  ```
</details>

</br></br>
<p>&copy abiabdillahx</p>
