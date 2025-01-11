#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7669473217:AAFFhjr0mQ0i1Q7j3CAGjq1azodcG0EdYPE")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21187550"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "640e8c81851bdedb930cb71a350a351a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002466275531"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8027481118"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://aarshhub:6L1PAPikOnAIHIRA@cluster0.6shiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AdultDatabase")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002281332202"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://envs.sh/vD5.jpg")
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n𝘐 𝘈𝘔 𝘊𝘖𝘕𝘛𝘌𝘕𝘛 𝘗𝘙𝘖𝘝𝘐𝘋𝘌𝘙 𝘉𝘖𝘛 😌 .\n𝘐 𝘞𝘐𝘓𝘓 𝘗𝘙𝘖𝘝𝘐𝘋𝘌  𝘉𝘌𝘚𝘛 𝘖𝘍 𝘊𝘖𝘕𝘛𝘌𝘕𝘛 𝘍𝘖𝘙 𝘠𝘖𝘜 ⚡️ .")
try:
    ADMINS=[8027481118]
    for x in (os.environ.get("ADMINS", "8027481118").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me🥰\n\nKindly Please join Channel✨️</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "10"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", " ")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", " ")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages. join @allvidsbackup1 !"

ADMINS.append(OWNER_ID)
ADMINS.append(5803610610)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
