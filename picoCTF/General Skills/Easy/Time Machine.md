# Time  Machine
### Author: Jeffery John

## Description
What was I last working on? I remember writing a note to help me remember...
You can download the challenge files here:
- [challenge.zip](https://artifacts.picoctf.net/c_titan/67/challenge.zip)


## Solution
This is a general **Git** skills challenge. After i unzip the zip file, i open the directory and listing all files there. There is only **"message.txt"** file and **".git"** directory.
Then, i try to open the message and just said _"This is what I was working on, but I'd need to look at my commit history to know why..."_. Then, what was coming to my head is "check the commit log". Yeah, just type this command and i got the flag.
```sh
$ git log
```
[gambar]


## Flag
<details>
    <summary>Click this!</summary>

```
picoCTF{t1m3m@ch1n3_5cde9075}
```

</details>
