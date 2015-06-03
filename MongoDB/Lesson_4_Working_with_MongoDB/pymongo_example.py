from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

tesla_s = {
    "manufacturer": "Tesla Motors",
    "class": "full-size",
    "body style" : "5-door liftback",
    "production" : [2012, 2013],
    "model years" : [2013],
    "layout" : ["Real-motor", "rear-wheel drive"],
    "designer" : {
        "firstname" : "Franz",
        "surname" : "von Holzhausen"
    },
    "assembly":[
        {
            "country" : "United States",
            "city" : "Fremont",
            "state" : "California"
        }
    ]
}

db = client.examples
db.autos.insert(tesla_s)

for a in db.autos.find():
    pprint.pprint(a)
