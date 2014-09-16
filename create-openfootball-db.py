import pymongo

client = pymongo.MongoClient()

#if 'openFootball' not in client.database_names():
db = client.open_football
collection = db.matches_collection