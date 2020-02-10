import pymongo
from typing import Dict


class Database(object):
    URI = "mongodb+srv://test:test@board-qkeln.gcp.mongodb.net/test?retryWrites=true&w=majority"
    DATABASE = pymongo.MongoClient(URI).get_database("Phishing")

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)
