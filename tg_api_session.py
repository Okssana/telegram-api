
from telethon.sync import TelegramClient


api_id = 'XXXXXXXXXXXXXXXXXXX'  # Replace with your API ID
api_hash = 'XXXXXXXXXXXXXXXXX'  # Replace with your API Hash


with TelegramClient('session_name', api_id, api_hash) as client:
    client.loop.run_until_complete(client.get_me())




