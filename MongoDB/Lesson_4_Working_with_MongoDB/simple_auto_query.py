from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples

def find():
    autos = db.autos.find({"manufacturer":"Toyota"})
    for a in autos:
        pprint.pprint(a)

if __name__ == '__main__':
    find()
