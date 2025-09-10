import os 
from enum import StrEnum
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection constants
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE_NAME = "cwru-wtf-db"

class CollectionNames(StrEnum):
    SCHEDULES = "schedules"
    ORGANIZATIONS = "organizations"