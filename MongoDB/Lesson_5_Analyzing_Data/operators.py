"""
Operators

$project
$match
$group
$sort
$skip
$limit
$unwind

Use $project to
- include fields from original document
- insert computed fields
- rename fields
- create fields that hold subdocuments
"""


def highest_ratio():
    result = db.tweets.aggregate([
        {"$match":{"user.friends_count" : {"$gt":0},
                   "user.followers_count" : {"$gt":0}}},
        {"$project":{"ratio":{"$divide":["$user.followers_count",
                                          "$user.friends_count"]},
                     "screen_name":"$user.screen_name"}},
        {"$sort":{"ratio":-1}},
        # return the highest ratio user
        {"$limit":1}])
    return result
                              

def user_mentions():
    result = db.tweets.aggregate([
        {"$unwind" : "$entities.user_mentions"},
        # create one copy for each array in user_mentions
        {"$group" : {"_id":"$user.screen_name",
                     "count":{"$sum":1}}},
        {"$sort" : {"count":-1}},
        {"$limit":1}])
    return result

"""
$group operators

$sum
$first
$last
$last
$max
$min
$avg

$push : add all values to an array
$addToSet : add the unique values to an array
"""

def unique_hashtags_by_user():
    result= db.tweets.aggregate([
        { "$unwind" : "$entities.hashtags"},
        { "$group" : {"_id" : "$user.screen_name",
                      "unique_hashtags" : {
                          "$addToSet" : "$entities.hashtags.text"
                        }}},
        { "$sort" : {"_id":-1}}])
    return result


def unique_user_mentions():
    result = db.tweets.aggregate([
        {"$unwind" : "$entities.user_mentions"},
        {"$group" : {
            "_id":"$user.screen_name",
            "mset":{
                "$addToSet":"$entities.user_mentions.screen_name"
            }}},
        {"$unwind":"$mset"},
        # 2nd group calculates the count we want
        {"$group": {"_id":"$_id", "count":{"$sum":1}}},
        {"$sort" : {"count":-1}},
        {"$limit":10}
        ])
    return result
