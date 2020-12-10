
# Walmart Auto Buy Bot

## Prereqs
- Python version 3.9
- once python is downloaded, open CMD and execute: pip install selenium
- chrome
- logged in Walmart account on chrome, make sure your address and credit card info is already in your account
- no opened chrome windows
- open WalmartAutoBuyBot/config.py
    - put the walmart URL of the product in product_url
    - in chrome in the URL put chrome://version/ and hit enter. Copy Profile Path into config.py's chrome_profile, make sure to use double \\ e.g. C:\\Users\\Silina\\AppData\\Local\\Google\\Chrome\\User Data\\
- go to https://chromedriver.chromium.org/downloads and download the chromedriver based on what chrome version you have (can find version here chrome://version/), unzip and put the chromedriver in dir WalmartAutoBuyBot

## Execution
- open CMD
- cd into dir WalmartAutoBuyBot
- execute python WalmartAutoBuyBot.py 
