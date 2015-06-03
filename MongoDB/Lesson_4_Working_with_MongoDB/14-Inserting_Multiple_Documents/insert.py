from autos import process_file
import os
os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Lesson_4_Working_with_MongoDB/14-Inserting_Multiple_Documents')
infile = 'auto-small.csv'


def insert_autos(infile, db):
    data = process_file(infile)

    # Your code here. Insert the data in one command
    # autos will be a list of dictionaries, as in the example in the previous video
    # You have to insert data in a collection 'autos'
    for line in data:
        db.autos.insert(line)


  
if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print db.autos.find_one()
