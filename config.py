import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29199850"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "711c12d4f9bb08a1342715862e4df9c9")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6486329379"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://aaka8h:D7isu9EqbguSB4Wt@cluster0.h95fe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "aaka8h")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
