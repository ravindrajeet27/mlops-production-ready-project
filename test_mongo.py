from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

uri = os.getenv("MONGODB_URL")

try:
    client = MongoClient(
        uri,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000
    )

    print(client.list_database_names())
    print("✅ Connected Successfully!")

except Exception as e:
    print(type(e).__name__)
    print(e)