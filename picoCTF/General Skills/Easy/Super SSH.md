# Super SSH
### Author: Jeffery John

## Description
_*Disclaimer: Launch the instance first!_
Using a Secure Shell (SSH) is going to be pretty important.
Can you ssh as `ctf-player` to `titan.picoctf.net` at port `52052` to get the flag?
You'll also need the password `passwd`. If asked, accept the fingerprint with yes.
If your device doesn't have a shell, you can use: https://webshell.picoctf.org
If you're not sure what a shell is, check out our Primer: https://primer.picoctf.com/#_the_shell

## Solution
It is just basic ssh connecting challenge, once u connected, u will get the flag. So, this is the command to connect with ssh :
```
$ ssh -p <port> ctf-player@titan.picoctf.net 
```

Change the _'<port>'_ with your port!

[gambar ss]

## Flag
<details>
  <summary>Ini yahh flag-nya</summary>

  ```
picoCTF{s3cur3_c0nn3ct10n_8306c99d}
  ```
</details>

<p>by abiabdillahx</p>
