import motor.motor_asyncio
from charger_messaging.config import DATABASE_URL


client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
database = client.sessions
session_collection = database.get_collection("session_collection")
