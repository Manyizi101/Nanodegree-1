#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
import os
os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Lesson_2_Problem_Set/02-Airport_List')
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        airport_list = soup.find(id = 'AirportList')
        for airport in airport_list.find_all('option'):
            if len(airport['value']) == 3 and airport['value'].isupper():
                data.append(airport['value'])

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
