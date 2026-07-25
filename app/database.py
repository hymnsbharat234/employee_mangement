from motor.motor_asyncio import AsyncIOMotorClient
import certifi
import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(
    MONGODB_URL,
    tlsCAFile=certifi.where(),
)

database = client[DATABASE_NAME]

def get_database():
    return database