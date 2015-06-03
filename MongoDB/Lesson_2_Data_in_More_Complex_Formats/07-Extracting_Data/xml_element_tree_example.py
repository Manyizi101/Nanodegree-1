import xml.etree.ElementTree as ET
import pprint
import os
os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Lesson_2_Data_in_More_Complex_Formats/07-Extracting_Data')


tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()

title = root.find('./fm/bibl/title')
title_text = ""

for p in title:
    title_text += p.text
print "\nTitle:\n", title_text

print "\nAuthor email addresses:"
for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    if email is not None:
        print email.text
