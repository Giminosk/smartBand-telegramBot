# Smart band data analysis with telegram bot

It's a simple [Telgram](https://web.telegram.org) bot I created to display some statistics from my smart band. I had trouble with the official application of my band, but I managed to get access to the collected data. This data is stored as a few CSV files and updates in a few minutes.

## Requirements:
  - `requirements.txt`
  - *Telegram’s Bot API* - which you can get [here](https://t.me/botfather)
  
## Results:  
<img src="/images/result/res1.png" width="200" height="400"/><img src="/images/result/res2.png" width="280" height="340"/>
<img src="/images/result/res3.png" width="220" height="400"/>  
<img src="/images/sleep2.png" width="400" height="200"/>
<img src="/images/activity.png" width="400" height="200"/>  
<img src="/images/heart.png" width="400" height="200"/>
<img src="/images/sleep1.png" width="250" height="250"/>

## File structure:
  - `data` is folder with updatable csv files with data
  - `images`  is folder with generated plots
    - result is folder with screenshots of final version bot
  - `utils` is folder with .py modules to analize data
  - `main.py` is main script with bot
