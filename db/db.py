from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "website_builder")


class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[DB_NAME]

        # Collections
        self.projects = self.db["projects"]
        self.templates = self.db["templates"]
        self.layouts = self.db["layouts"]

    # ---------- Helper ----------
    def serialize(self, data):
        if isinstance(data, list):
            return [self.serialize(item) for item in data]
        if isinstance(data, dict):
            data["_id"] = str(data["_id"])
            return data
        return data

    # ---------- INSERT ----------
    async def insert_one(self, collection, data):
        result = await collection.insert_one(data)
        return str(result.inserted_id)

    # ---------- FIND ONE ----------
    async def find_one(self, collection, query):
        data = await collection.find_one(query)
        return self.serialize(data) if data else None

    # ---------- FIND ALL ----------
    async def find_all(self, collection, query={}):
        cursor = collection.find(query)
        results = []
        async for doc in cursor:
            results.append(self.serialize(doc))
        return results

    # ---------- UPDATE ----------
    async def update_one(self, collection, query, new_values):
        return await collection.update_one(query, {"$set": new_values})

    # ---------- DELETE ----------
    async def delete_one(self, collection, query):
        return await collection.delete_one(query)

    # ---------- ObjectId Helper ----------
    def to_object_id(self, id_str):
        return ObjectId(id_str)


# Singleton instance
db = MongoDB()