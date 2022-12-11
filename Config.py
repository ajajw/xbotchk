import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    OWN_ID = int(os.environ.get('OWN_ID', 0))
    
else:
    # Fill the Values
    API_ID = 2482978
    API_HASH = "8e07b78d4a879cfc4f74770e1b3bc542"
    BOT_TOKEN = "5130502871:AAE1fFWFqgMetuSI679qZHtykofU6yY7zJk"
    DATABASE_URL = "postgresql://postgres:EvF8WoZIi2MARmF9TAPR@containers-us-west-44.railway.app:6483/railway"
    OWN_ID = 5032070399
    
