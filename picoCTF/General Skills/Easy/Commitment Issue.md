# Commitment Issue
### Author: Jeffery John

## Description
What was I last working on? I remember writing a note to help me remember...
You can download the challenge files here:
- [challenge.zip](https://artifacts.picoctf.net/c_titan/67/challenge.zip)


## Solution
So, unzip it first, then list all files there. There are only **message.txt** file and **.git** folder. After that, i check the commit history using this command
[gambar]

Yeah, there is first commit said 'create flag'. We just have to checkout to that commit code. This is the reference to learn more about git : [docs](https://git-scm.com/docs).
Actually, the 'message.txt' file isn't commited yet, so I use these command to create a new branch to commit it and checkout to the first commit.
```sh
git add .
git commit -m "anything"
git checkout -b test-branch ea859bf3b5d94ee74ce5ee1afa3edd7d4d6b35f0
cat message.txt
```
[gambar]


## Flag
<details>
    <summary>This is the flag!</summary>

```
picoCTF{s@n1t1z3_cf09a485}
```

</details>
