
#check whether a variable exist:

db.cities.find({"governmentType" : {"$exist" : 1}}).count()

#regular expression:
db.cities.find({"motto":{"$regex": "[Ff]riendship|[Pp]ride"}}).count()

#$in operator:
db.autos.find({"modelYears" : {"$in" : [1965, 1966, 1967]}}).count()

#$all operator: (all contains the list)
db.autos.find({"modelYears" : {"$all" : [1965, 1966, 1967]}}).count()

# query inside a dictionary (dot operator)
db.autos.find({"dimensions.weight" : {"$gt":5000}}).count()

# only show the text
db.tweets.find({"entities.hashtags" : {"$ne" : []}},{"entities.hashtags.text":1,"_id":0})

# find_one: returns the first document of query
db.cities.find_one({"name" : "Munchen",
                    "country" : "Germany"})

# update single document
# $set: if not in the document, add it; if in, update info
db.cities.update({"name" : "Munchen",
                    "country" : "Germany"},
                 {"$set":{
                     "isoCountryCode" : "DEU"
                 }})

# $unset: delete it
db.cities.update({"name" : "Munchen",
                    "country" : "Germany"},
                 {"$set":{
                     "isoCountryCode" : ""
                 }})

# save command to update
city = db.cities.find_one({"name" : "Munchen",
                    "country" : "Germany"})
city['isoCountryCode'] = 'DEU'
db.cities.save(city)

# update multiple documents at once
db.cities.update({"name" : "Munchen",
                    "country" : "Germany"},
                 {"$set":{
                     "isoCountryCode" : "DEU"
                 }},
                 multi = True)

# remove / drop
db.cities.remove({"name":"Chicago"})

# cities don't have a name, remove them
db.cities.find({"name" : {"$exists":0}}).count()
db.cities.remove({"name" : {"$exists":0}})
