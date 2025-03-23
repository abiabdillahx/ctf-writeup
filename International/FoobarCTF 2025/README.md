# FoobarCTF 2025
CTFTime : https://ctftime.org/event/2720

Date : 	22 March, 13:30 UTC+7 — 23 March 2025, 13:30 UTC+7

> [!NOTE]
> Capturing the flag solo by **_zenCipher_** usn

<details>
    <summary><b>Table of contents</b></summary>

1. [General](#-general)
   - [CryptoMix Madness](#cryptomix-madness)
   - [Silent Whispers](#silent-whispers)
   - [Lost Transmission](#lost-transmission)
2. [Reverse Engineering](#-reverse-engineering)
   - [Bitmap Mystery](#bitmap-mystery)
3. [Web Exploitation](#-web-exploitation)
   - [Silent Override](#silent-override)
</details>

# ✨ General
## CryptoMix Madness
### Description
> A brilliant cryptographer once designed a secret verification system to protect valuable information. The system, known as CryptoMix Madness, uses a series of transformations to encode the final message.
>
>To prove your cryptographic prowess, you must correctly apply the some transformations.
>
>Can you crack the code and claim the ultimate reward?
``nc chall.foobarctf.nitdgplug.org 31337``

**Hint :**
> - Some transformations can be reversed, others cannot. Choose your methods wisely.
> - If you can’t read it, maybe the alphabet has shifted?

**Attachment** : [Hint.txt](./files/Hint.txt)

### Solve
To solve this challenge, we need to apply the transformations in the correct order written in **Hint.txt**. When i tried to connect netcat, it asked me some questions to get the flag.
So, i use a tool that can help me to solve the problem. I used [CyberChef](https://gchq.github.io/CyberChef/). Just input the asked text, then apply the encoding method respectively.
1. Base64 of "FoobarCTF" = "Rm9vYmFyQ1RG"
2. MD5 Hash of "GLUG" = d8d3b7ff9b42d918aa88ac1d3b654b33
3. SHA-256 Hash of "UBUNTU" = 28ddb685efc574520b007ba79f0d3ae0746ee51401a1e894f8b86f1c1afec13d
4. ROT13 of "LINUX" = "YVAHK"
4. Hexadec representation of "OPEN_SOURCE" = 4f50454e5f534f55524345

[gambar ss]

Boom!, i got the flag!
**Flag:**
```flag
GLUG{Crypto_Transformation_Master}
```

## Silent Whispers
### Description
> A cryptic image was intercepted from an underground hacker forum—hearme.jpg. At first glance, it appears to be just an ordinary picture, but intelligence reports suggest otherwise.
>
> The sender, known only as "GhostCipher," is infamous for embedding secret messages in plain sight. Rumors say that critical information has been hidden within this image, accessible only to those who know where to look.
>
> Can you decode the hidden message before it vanishes into the void?

**Attachment** : [hearme.jpg](./files/hearme.jpg)

### Solve
Ok, let's try to see if this jpg fil ehas steganography in it. It will be extracted to a text file that has a link to google drive
[gambar ss]

After that, just download the file. It's an audio file and sounds like write a spectrogram there. So, i open it with [**audacity**](https://audacityteam.org/) and change view mode to spectrogram. Wow, it has a less readable text there. It's look like Base64 encoded text, just decode it and you will get the flag!
[gambar ss]


**Flag:**
```flag
GLUG{A@ud!o_3ncRypt_9x7#}
```

## Lost Transmission
### Description
> A rogue operative was transmitting classified data when their signal was intercepted. Our analysts recovered only a single file from the transmission—final_challenge.mp3.
>
> However, something feels off. No traces of audio data exist in the file, and attempts to play it result in static. The intelligence agency believes that the operative may have used unconventional methods to conceal the data.
>
> Your mission is to uncover what lies within and retrieve the lost information before it disappears forever.

**Hint :**
> - Layers upon layers—peel them back carefully.
> - Not everything is as it seems. Look beyond the obvious.

**Attachment** : [final_challenge.mp3](./files/final_challenge.mp3)


### Solve
1. Based on the hint, i think this file has a hidden file in it. SO, i just use `steghide` to extract it. 
```sh
steghide extract -sf final_challenge.zip
```
2. Then, it will gave me a file with **.out** extension. It is actually RAR file. Unrar it. 
```sh
unar final_challenge.out.rar
```
3. After that, i got `flag.7z` file. After extract the 7z file, it gave me `flag.tar.gz` (damnn, wtf is this layers). 
```sh
7z x flag.7z
tar -xvzf flag.tar.gz
```
4. Ok, extract it too and i got the last layer, `flag.zip`. Just unzip it and the real flag shown.

**Flag:**
```flag
GLUG{UnZ1pp1nG_N1ghtmar3}
```

# 🔀 Reverse Engineering
## Bitmap Mystery
### Description
> You have intercepted a mysterious BMP file, but its contents seem to be encoded. Your task is to analyze the given Python script and extract the hidden flag from flag.bmp.

**Hint :**
> - The script reads flag.bmp and processes pixel data using bitwise operations.
> - Pay close attention to how the script manipulates pixel intensity and encodes information—this might be a form of steganography!

**Attachment** : [compressed_data](./files/compressed_data) and [compressed.py](./files/compressed.py)

### Solve
After analyzed it, it is can be reversed by this steps
1. Read the BMP header (54 bytes) and compressed data.
2. Reverse RLE: Expand bytes based on their count to reconstruct the XORed data.
3. Reverse XOR (byte ^ 0xAA) to restore the original pixel data.
4. Save the result (header + decompressed data).

Here is the script :
```python
def decompress_bmp(input_file, output_file):
    with open(input_file, "rb") as f:
        header = f.read(54)  # BMP header (first 54 bytes)
        compressed_data = f.read()  # Read compressed pixel data

    decompressed_data = bytearray()
    
    # Reverse the run-length encoding (RLE)
    i = 0
    while i < len(compressed_data):
        byte = compressed_data[i]
        count = compressed_data[i + 1]
        decompressed_data.extend([byte] * count)
        i += 2  # Move to the next (byte, count) pair

    # Reverse the XOR transformation
    original_data = bytearray(b ^ 0xAA for b in decompressed_data)

    with open(output_file, "wb") as f:
        f.write(header)  # Write BMP header
        f.write(original_data)  # Write decompressed pixel data

    print(f"Decompression complete. Decompressed size: {len(original_data)} bytes")

if __name__ == "__main__":
    decompress_bmp("compressed_data", "decompressed_flag.bmp")


```
**Flag:**
```flag
GLUG{Bm9_R8VreVers3}
```


# 🌐 Web Exploitation
## Silent Override
### Description
> The system trusts its tokens a little too much. An /api/admin endpoint hides the flag, but your token says you’re not worthy. Can you bend the rules and claim what’s hidden?
>
> http://chall.foobarctf.nitdgplug.org:31302

### Solve
This is the first look of the web's chall.
[gambar ss]

There is an login form. So, what i did firstly is try to log in with random username and password. It gives me a **JWT Token** under it. Hmm, interesting. Try to decode the JWT token with [JWT.io](https://jwt.io/). Just paste my token and it said that the value of "admin" attribute is _false_. 
[gambar ss]

Ok. i chamged the 'admin' value to _true_, and then copy the new encoded JWT token. Back to the website, then open inspect element or dev mode ("**Ctrl+Shift+I**"). Damn, there is a commented out code in the login form. It seems like a button that will put admin data there.
[gambar ss]

After that, i try to input my new JWT token by removing "readonly" attribute from the input field. Then, i click the button. And... i got the flag.
[gambar ss]


**Flag:**
```flag
GLUG{JWT_Manipulation_Success}
```



========================================================


Thanks for read this writeup. If u wanna support me, buy me a coffee [here](https://ko-fi.com/abiabdillah) or click button below

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/abiabdillah) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/abiabdillah)