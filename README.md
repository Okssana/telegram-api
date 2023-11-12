# telegram-api

There are two ways to fetch data from Telegram:

1) With an API (contains more info including statistics).

2) Download manually from an installed application (Mac Pro only as far as I know). Go to the channel you want to fetch. Find three dots on the header of a channel. Click "Export chart history". It has several options: HTML/JSON, date range, types of files. It will save data to your laptop in the folder called f"ChatExport_{date}"

In this repo there is .ipynb file where a chat history in html format was parsed. 


# Step-1: Register a TG account


# Step-2: Create an application

https://my.telegram.org/auth?to=apps
https://my.telegram.org/apps

A hint: don't use a VPN. It fails, when you are connected to VPN. 

Obtain an App configuration:

- App api_id:
- App api_hash:

We need them to create a session in our Python code. 


# Step-3

In the file *tg_api_session.py* we establish a session.

In the terminal run a command python3 *tg_api_session.py* which is going to create a session file with credentials and a session's info.

After this we can move to *tg_api_data.ipynb* file and fetch the actual data. 
