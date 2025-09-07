from src.database.connection.constants import (
    MONGO_URI,
    MONGO_DATABASE_NAME,
)
from mongoengine import connect

connect(
    db=MONGO_DATABASE_NAME,
    host=MONGO_URI,
    connect=False,  
)

