from pymongo.mongo_client import MongoClient
from data import config as cfg

client = MongoClient(cfg.URI)

db = client['sentiment_analysis']
collection = db['results']

def insertResults(results):
    if results:
        try:
            collection.insert_many(results)
            print("Results successfully inserted into MongoDB")
        except Exception as e:
            print(f"Error inserting results into MongoDB: {e}")
