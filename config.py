#---------- © sᴛᴀʟᴋᴇʀ@hehe_stalker
#---------- ᴘʀᴏJᴇᴄᴛ - ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ sᴇʟʟɪɴɢ ʙᴏᴛ
#-------------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()

def _getenv(name: str, default: str | None = None, required: bool = False) -> str:
    val = os.getenv(name, default)
    if required and (val is None or val == ""):
        raise RuntimeError(f"Missing required env var: {name}")
    return val

UPDATES_CHANNEL_ID = -1004199515021
UPDATES_CHANNEL_LINK = "https://t.me/+1wQbCvn9VZk4OGRl"
SUPPORT_CHANNEL_ID = -1004485862613
SUPPORT_CHANNEL_LINK = "https://t.me/+sxG9N_RVqvZjNTNl"
MUST_JOIN_CHANNEL = str(UPDATES_CHANNEL_ID)

# Bot token: இங்கே உங்கள் token-ஐ மாற்றிக்கொள்ளுங்கள்
BOT_TOKEN = _getenv("BOT_TOKEN", "8830257783:AAHMaJww6ekNmWTUaZcH_5gNlU8y6vIx5UA", required=True)

ADMIN_IDS = [int(i) for i in _getenv("ADMIN_IDS", "7973967415", required=True).replace(" ", "").split(",") if i]
API_ID = "31724382"
API_HASH = "cdaa5c6f43ec7eccbe7142d25e6e1c67"
# bot.py reads these from os.environ
os.environ.setdefault("API_ID", API_ID)
os.environ.setdefault("API_HASH", API_HASH)

DATABASE_URL = _getenv("DATABASE_URL", "mongodb+srv://OtpWala:PapaiPaul13@otpwala.gjxwbr3.mongodb.net/?appName=OtpWala")

DEFAULT_CURRENCY = _getenv("DEFAULT_CURRENCY", "₹")
MIN_BALANCE_REQUIRED = float(_getenv("MIN_BALANCE_REQUIRED", "0"))