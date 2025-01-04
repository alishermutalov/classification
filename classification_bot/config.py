from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")
