from pymongo import MongoClient
import pprint

"""
Ineuqality operators
$gt
$lt
$gte
$lte
$ne
"""

client = MongoClient('mongodb://localhost:27017/')

db = client.examples

def find():

    query = {"population" : {"$gt" : 250000, "$lt": 500000}}
    #query = {"name" : {"$gte" : "X", "$lt": "Y"}}
    #query = {"foundingDate":{"$gte":datetime(1837,1,1),
    #                         "$lte":datetime(1837,12,31)}
    #query = {"country":{"$ne":"United States"}}
    cities = db.cities.find(query)

    num_cities = 0
    for c in cities:
        pprint.pprint(c)
        num_cities += 1

    print "\nNumber of cities matching: %d\n" % num_cities
