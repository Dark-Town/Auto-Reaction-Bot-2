import os

API_ID = os.getenv("24413166", "")
API_HASH = os.getenv("7d43dfedf3baa98292adb7b3f69cd6bd", "")
BOT_TOKEN = os.getenv("8104653263:AAGBJug5XeN09C4h-bkjTjdSDwzHNJHB9vc", "")
ADMIN = int(os.getenv("ADMIN", ""))

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))

DB_URI = os.getenv("mongodb+srv://thelastcroneb:Tcroneb/2025@jinwoo.zvygv0t.mongodb.net/?retryWrites=true&w=majority&appName=jinwoo", "")
DB_NAME = os.getenv("jinwoo", "")

IS_FSUB = bool(os.environ.get("FSUB", False)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
