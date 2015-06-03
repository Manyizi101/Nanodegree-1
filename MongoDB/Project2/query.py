import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.openmap

# number of documents
db.austin.find().count()

# number of nodes
db.austin.find({'type':'node'}).count()

# number of way
db.austin.find({'type':'way'}).count()

# number of unique users
db.austin.distinct('created.user').length

## Number of users appearing only once
db.austin.aggregate([
    {"$group":{"_id":"$created.user", "count":{"$sum":1}}},
    {"$group":{"_id":"$count", "num_users":{"$sum":1}}},
    {"$sort":{"_id":1}},
    {"$limit":10}
    ])

# Top contributor
db.austin.aggregate([
    {"$group":{"_id":"$created.user", "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":1}
    ])

# Top 10 amenities
db.austin.aggregate([
    {"$match": {"amenity": {"$exists":1}}},
    {"$group": {"_id": "$amenity", "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
    ])

# Biggest religion
db.austin.aggregate([
    {"$match": {"amenity": {"$exists":1}, "amenity":"place_of_worship"}},
    {"$group": {"_id":"$religion", "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$ne":null},
    {"$limit":1}
    ])

# Most popular cuisines
db.austin.aggregate([
    {"$match": {"amenity": {"$exists":1}, "amenity":"restaurant"}},
    {"$group": {"_id":"$cuisine", "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":5}
    ])


# Top 5 fast food
db.austin.aggregate([
    {"$match": {"amenity": {"$exists":1}, "amenity":"fast_food"}},
    {"$group": {"_id":"$name", "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":5}
    ])

# Most popular gas station
db.austin.aggregate([
    {"$match": {"amenity": {"$exists":1}, "amenity":"fuel"}},
    {"$group": {"_id":"$name", "count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":1}
    ])
