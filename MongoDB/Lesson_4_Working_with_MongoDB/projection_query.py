from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples

def find():
    query = {"manufacturer":"Toyota", "class":"mid-size car"}
    projection = {"_id" : 0, "name" : 1}
    autos = db.autos.find(query, projection)
    for a in autos:
        pprint.pprint(a)

if __name__ == '__main__':
    find()
