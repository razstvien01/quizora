from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

MONGODB_URI = config("MONGODB_URI")
client = AsyncIOMotorClient(MONGODB_URI)
db = client[config("MONGODB_NAME", default="mockquiz_mongo")]

thread_collection = db.threads
comments_collection = db.comments
reactions_collection = db.reactions
notifications_collection = db.notifications