
# Manual for Telegram API

There are two ways to fetch data from Telegram:

1. With an API (contains more info including statistics).
2. Download manually from an installed application (Mac Pro only as far as I know). Go to the channel you want to fetch. Find three dots on the header of a channel. Click "Export chart history". It has several options: HTML/JSON, date range, types of files. It will save data to your laptop in the folder called f"ChatExport_{date}"

In this repo there is .**ipynb** file where a chat history in html format was parsed.

### Step-1: Register a TG account

[](https://github.com/Okssana/telegram-api#step-1-register-a-tg-account)

### Step-2: Create an application

[https://my.telegram.org/auth?to=apps](https://my.telegram.org/auth?to=apps)[https://my.telegram.org/apps](https://my.telegram.org/apps)

A hint: don't use a VPN. It fails, when you are connected to VPN.

Obtain an App configuration:

* App api_id:
* App api_hash:

We need them to create a session in our Python code.

### Step-3: Gather data

TG channels:

In the file **`tg_api_session.py`** we establish a session.

Install a library:

```
pip install telethon
```

In the terminal run a command:

```
python3 tg_api_session.py
```

which is going to create a session file with credentials and a session's info.

After this we can move to `tg_api_data.ipynb` file and fetch the actual data.Step-4

`tg_api_forw.ipynb`  contains a code for obtaining forwarded messages

`tg_api_data.ipynb` contains the basics of API.

### Step-4: Build Network. Analyze TG stats. 

After we are done with downloading TG channels in `tg_api_forw.ipynb`, we can move forward to building a data frame needed for Gephi. 

Open `tg_api_forw_network.ipynb`

### Step-5: Working with data

In order to work with data obtained by the method* **"Export chat history"** *using an app, open the Jupiter notebook `chat_Rosich.ipynb` which contains:

* Cleaning,
* Time analysis,
* Extraction of entities,
* Text analysis (where we use stopwords).

Furthermore, code is universal, so you can apply it to any of TG channels.

### Step-6: TG channels

The list of TG channels.

https://docs.google.com/spreadsheets/d/1Mkn46uMcwH0-aHck0A389xbbCyfqXfQ2X5oSi9wLlEY/edit?usp=sharing


### Users by location

`tg_api_users_by_location.py`

Set a long and a lat for you location and gather users nearby this point. 

## **Technical setup**

**Create a virtual environment: in my case it's  `tg_api_tool. `**

An example of activation a virtual environment:

```
pyenv virtualenv 3.10.6 tg_api_tool
```

## Errors

Unresolved:

*Telegram is having internal issues RpcCallFailError: Telegram is having internal issues, please try again later. (caused by GetHistoryRequest)*



To be continued.

## Stopwords for a ru language

**stopwords_emails_ru**.**py** contains stop words in ru language. It combines several publicly avaliable datasets and stopwords I've added manually.
