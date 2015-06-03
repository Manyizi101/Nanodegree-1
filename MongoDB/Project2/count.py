"""
This python file counts the summary of the Austin map dataset.
It will return the total number of node names.
"""

import xml.etree.cElementTree as ET
import pprint
import os
os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Project2')
filename = 'austin_texas.osm'

def count_tags(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        index = ['bounds','member','nd','node','osm','relation','tag','way']
        tags = {}
        for i in index:
            count = 0
            for j in root.iter(i):
                count = count + 1
            tags[i] = count
        
        return tags        


tags = count_tags(filename)
pprint.pprint(tags)

