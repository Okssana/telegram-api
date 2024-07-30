

from telethon import TelegramClient, events, errors
from pprint import pprint
import asyncio

from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetLocatedRequest
from telethon.tl.types import InputGeoPoint
import csv
import os

import time


import sqlite3

# Define your Telegram API credentials

api_id = 'API_ID'  # Replace with your API ID
api_hash = 'API_HASH'

bot_token = 'BOT_TOKEN'  # Replace with your bot token

#client = TelegramClient('session_name_oksana', api_id, api_hash)

session_name = f'session_{int(time.time())}'
print("Session name:", session_name)
client = TelegramClient(session_name, api_id, api_hash)
print(client)

# Location coordinates
latitude = 48.518041
longitude = 37.952584



name_of_location = 'Name_of_Location'


location = f'{name_of_location}_{latitude}_{longitude}'
session_name = 'session_name_oksana'

for attempt in range(5):  
    try:
        with TelegramClient(session_name, api_id, api_hash) as client:
            client.start()
            geo_point = InputGeoPoint(lat=latitude, long=longitude)
            result = client(GetLocatedRequest(geo_point), 1000, 10)
            print(result, "\n")

            if result:
                # Open a CSV file to write the user data
                with open(f'nearby_users_results_{name_of_location}.csv', 'w', newline='', encoding='utf-8') as csvfile:

                    fieldnames = ['id', 'is_self', 'contact', 'mutual_contact', 'deleted',
                                'bot', 'bot_chat_history', 'bot_nochats', 'verified', 'restricted',
                                'min', 'bot_inline_geo', 'support', 'scam', 'apply_min_photo', 
                                'fake', 'bot_attach_menu', 'premium', 'attach_menu_enabled', 'bot_can_edit',
                                'close_friend', 'stories_hidden', 'stories_unavailable', 'contact_require_premium',
                                'bot_business', 'access_hash', 'first_name', 'last_name', 'username',
                                'phone', 'photo', 'status', 'bot_info_version', 'restriction_reason', 'bot_inline_placeholder',
                                'lang_code', 'emoji_status', 'usernames', 'stories_max_id', 'color', 'profile_color',
                                'latitude', 'longitude', 'timestamp']
                    
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    
                    # Write the header
                    writer.writeheader()
                    
                    # Iterate through the list of users and extract their info
                    for user in result.users:
                        writer.writerow({
                            'id': user.id,
                            'is_self': user.is_self,
                            'contact': user.contact,
                            'mutual_contact': user.mutual_contact,
                            'deleted': user.deleted,
                            'bot': user.bot,
                            'bot_chat_history': user.bot_chat_history,
                            'bot_nochats': user.bot_nochats,
                            'verified': user.verified,
                            'restricted': user.restricted,
                            'min': user.min,
                            'bot_inline_geo': user.bot_inline_geo,
                            'support': user.support,

                            'scam': user.scam,

                            'apply_min_photo': user.apply_min_photo,
                            'fake': user.fake,
                            'bot_attach_menu': user.bot_attach_menu,
                            'premium': user.premium,
                            'attach_menu_enabled': user.attach_menu_enabled,
                            'bot_can_edit': user.bot_can_edit,

                            'close_friend': user.close_friend,
                            'stories_hidden': user.stories_hidden,
                            'stories_unavailable': user.stories_unavailable,
                            'contact_require_premium': user.contact_require_premium,
                            'bot_business': user.bot_business,

                            'access_hash': user.access_hash,

                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'username': user.username,
                            'phone': user.phone,
                            'photo': user.photo,
                            'status': user.status,
                            'bot_info_version': user.bot_info_version,

                            'lang_code': user.lang_code,
                            'emoji_status': user.emoji_status,
                            'usernames': user.usernames,
                            'stories_max_id': user.stories_max_id,
                            'color': user.color,
                            'profile_color': user.profile_color,

                            # Location data
                            'latitude': latitude,
                            'longitude': longitude,
                            'timestamp': int(time.time())
                        })


    except sqlite3.OperationalError as e:
        print(f"SQLite error occurred: {e}. Retrying...")
        time.sleep(5) 


