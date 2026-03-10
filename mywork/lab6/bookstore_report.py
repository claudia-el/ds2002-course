from pymongo import MongoClient, errors
from bson.json_util import dumps
import pprint
import os




uri = os.getenv('MONGODB_ATLAS_URL')
username = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PWD')

client = MongoClient(uri, username=username, password=password, connectTimeoutMS=200, retryWrites=True)
db = client.bookstore
items = db.authors

if __name__ == "__main__":
    
    total_authors = db["authors"].count_documents({})
    print(f"Total authors: {total_authors}\n")

    for a in items.find({}, {"name": 1, "nationality": 1}):
        print(f"{a.get('name', 'Unknown')} ({a.get('nationality', 'Unknown')})")

