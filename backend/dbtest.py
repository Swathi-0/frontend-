from pymongo import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
dbname = os.getenv("MONGODB_DBNAME")

# URL encode the username and password
username = quote_plus(username)
password = quote_plus(password)

# Use the username and password in your connection string
mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.n7rjs.mongodb.net/{dbname}?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)

# Test the connection
try:
    client.admin.command('ping')
    print("MongoDB connection successful!")
except Exception as e:
    print("MongoDB connection failed:", e)
