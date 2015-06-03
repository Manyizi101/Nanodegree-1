"""
This file will return a set of unique users in the Austin Map dataset
"""
import xml.etree.cElementTree as ET
import pprint
import re
import os
os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Project2')
filename = 'austin_texas.osm'

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way" or element.tag == "relation":
            users.add(element.attrib['uid'])

    return users


users = process_map(filename)
print(len(users))
