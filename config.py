import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "19302621"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be663997dc5845b6cba859db10386cce")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://LazeMint:<db_password>@cluster0.vsfvv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
