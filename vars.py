#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "1922259"))
API_HASH = environ.get("API_HASH", "df46b4bda20f16abe680979c9639d702")
BOT_TOKEN = environ.get("BOT_TOKEN", "1807579706:AAHTj5_RTK0n1roz-5rj4GlDihmmS3xycHI")

OWNER = int(environ.get("OWNER", "1591043415"))
CREDIT = environ.get("CREDIT", "Marcus")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1591043415').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1591043415').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
