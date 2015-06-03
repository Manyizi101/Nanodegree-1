"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import os
os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Project2')


OSMFILE = 'austin_texas.osm'
#street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place",
            "Square", "Lane", "Road", "Trail", "Parkway", "Commons", "Circle",
            "Cove"]


mapping = { "Ave": "Avenue",
            "Ave.": "Avenue",
            "Avene":"Avenue",
            "Blvd" : "Boulevard",
            "Blvd." : "Boulevard",
            "CR" : "Court",
            "Cir" : "Circle",
            "Ct" : "Court",
            "Cv" : "Cove",
            "Dr":"Drive",
            "Dr.":"Drive",
            "Ln" : "Lane",
            "lane" : "Lane",
            "RD" : "Road",
            "Rd.": "Road",
            "Rd": "Road",
            "Pkwy":"Parkway",
            "St": "Street",
            "St.": "Street",
            "street":"Street",
             
             'IH ': 'Interstate Highway ',
             'I ': 'Interstate Highway ',
             'Interstate ': 'Interstate Highway ',
             'HWY ': 'Highway ',
             'Hwy ': 'Highway ',
             'Bldg ' : 'Building ',
             'Bldg. ': 'Building ',
             'Bld ': 'Building ',
             'Ste. ': 'Suite ',
             'Ste,' : 'Suite ',
             'STE ': 'Suite ',
             'S ': 'South ',
             'S. ': 'South ',
             'N ': 'North ',
             'N. ': 'North ',
             'W ': 'West ',
             'W. ': 'West ',
             'E ': 'East',
             'E. ': 'East',

            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    return street_types


def update_name(name, mapping):

    # Our street types contain numbers, cannot use street_type_re
    for key in mapping.keys():
        if key in name:
            name = name.replace(key, mapping[key])
            
    return name

st_types = audit(OSMFILE)
print(len(st_types))
pprint.pprint(dict(st_types))

##for st_type, ways in st_types.iteritems():
##    for name in ways:
##        name = update_name(name, mapping)


