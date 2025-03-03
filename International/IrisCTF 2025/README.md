# IrisCTF 2025 Writeup

## OSINT

### OSINT DISCLAIMER
**Description**
> The challenges this year does not require you to contact anyone. There will be no social media accounts needed to solve these challenges. Please refrain from reaching out to individuals on social media or contacting restaurants to inquire about further details. Such actions are unnecessary and will result in consequences leading to disqualification. Solving this challenge will unlock the rest of the Open-Source Intelligence category.

**Solve**
This is just like sanity check chall.

```
flag: irisctf{sp01l_f00d_1s_b4d_mk4y}
```

### Checking Out of Winter

**Description** </br>
> We took our annual road trip to Baja California Sur to visit the beach and play some golf. I like how this location is farther from the city compared to other resorts. I really enjoyed the sweet and savory sauce on the pizza with shredded chicken. After eating, I fell asleep, and half of my legs ended up getting tanned.

Question: Which hotel did Adam stay at? </br>
Link : https://osint-food-blog-web.chal.irisc.tf/pizza-by-the-water/

**Solve**
So, basically we just search for the hotel in Baja California Sur with golf course and pizza with shredded chicken. I find about "Baja California Sur first because idk what it is. But, when i search resorts in that area, it has so many resorts with **golf** and **beach**.
![Hotel in BCS area](https://github.com/user-attachments/assets/c9312584-277e-40b8-85fb-0c4004861be3)
I have tried almost all of golf resorts in Baja California Sur, especially from this [blog](https://www.tripadvisor.com/HotelsList-Baja_California-Golf-Resorts-zfp7841950.html). Until i found the correct one, it is **"Hilton Los Cabos Beach and Golf Resort"**. I was using this word in google search
![image](https://github.com/user-attachments/assets/e21aa9e0-139c-4a46-b6c9-6d569bec9c4f)
Damnn, i got the flag.

```
flag : irisctf{Hilton_Los_Cabos_Beach_and_Golf_Resort}
```
### Sleuths and Sweets
**Description**
> I visited my friend in Japan, and we had some alright crepes! The area had a lot of foot traffic, so we expected a long wait, but it was worth it. I’m usually not a fan of yogurt in my crepe, but it still tasted pretty alright.

Question: What is the address of this location? </br>
Blog Link : https://osint-food-blog-web.chal.irisc.tf/sleuths-and-sweets/

**Solve**
From the blog, i found a picture that maybe can be a "signature" of a shop or a restaurant. It's **Price Tag**. 
![image](https://github.com/user-attachments/assets/b3b73c2f-41d8-449b-af87-fde1bb6f698d)
I search the photo with _Google Lens_, the i found this price-tag is from "Marion Crepe" in Japan. So, i thought it just has one shop. So, i thought it's Marion Crepe in Ueno Ameyoko, then i realized the clue for this chall, `"The area had a lot of foot traffic"`. So, that's Shibuya, right?! I found a website that helps tourist in japan to search anything, [_JapanTravel_](https://japantravel.navitime.com/en/area/jp/search/?word=marion%20crepe).
![Screenshot 2025-01-06 110059](https://github.com/user-attachments/assets/758e7a26-b5af-41f5-93c8-27f747efc3f1)
Damn, Marion Crepe has many shop. So, I tried it one by one and got the right address in Jinnan, Shibuya.

```
flag : irisctf{1_Chome_21_3_Jinnan_Shibuya}
```


### Late Nite Bite
**Description**
> Some nights, I enjoy walking out to this modern local izakaya restaurant. They close pretty late, which makes it perfect for a late night snack. What makes this place unique is their dedication to brewing their own teas and constantly experimenting with new dishes on the menu. I like to order their mocktail Shiso Dry as my drink. As for meal spicy tuna onigiri with a bowl of miso soup is enough for me.
> I just want to show my appreciation and admiration for this place. But you guys will never find it! I regularly come here during the weekends.

**Solve**
Ok, i will say this challenge sucks. At first, i thought izakaya restaurant is literally in Japan. So i search any popular izakaya restaurant in Japan without any clue. Then, i realized there is an 'about' page in Adam's blog. He said "I’m Adam Holmes, a food blogger based in Southern California" and provide an image of his town.
![image](https://github.com/user-attachments/assets/ba50afa9-4a31-4cd2-b9c2-beb5efbc4182)
So, i just use google lens and found out that he lives in Santa Monica, California. I tried to search with all keywords that i have, "izakaya", "santa monica", "mocktail shiso dry". I found a blog that write about it [here](https://www.yelp.com/search?find_desc=Izakaya&find_loc=Santa+Monica%2C+CA). Then i found this [post](https://www.instagram.com/shirube_santamonica/p/DELJLUWO7Ip/). Damn, it's the right place!!
So, **Shirube** is the answer
```
flag : irisctf{Shirube}
```

Support me by buy me a [coffee](https://ko-fi.com/abiabdillah) or click this </br>
<a href="https://ko-fi.com/abiabdillah" style="text-align: center;"><img align="center" width="150" alt="support_me_on_kofi_blue" src="https://github.com/user-attachments/assets/c0fa4650-315c-4a4a-b1e3-76131e9eb8b8" /></a>


[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/abiabdillah) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/abiabdillahx)
<!-- [!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.ko-fi.com/abiabdillah) -->

