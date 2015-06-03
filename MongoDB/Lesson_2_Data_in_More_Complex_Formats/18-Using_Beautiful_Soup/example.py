import bs4
import os

os.chdir('/Users/Cinkie/Documents/Nanodegree/MongoDB/Lesson_2_Data_in_More_Complex_Formats/18-Using_Beautiful_Soup')

def options(soup, id):
    option_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values

def print_list(label, codes):
    print "\n%s:" % label
    for c in codes:
        print c

def main():
    soup = bs4.BeautifulSoup(open("page_source.html"))

    codes = options(soup, 'CarrierList')
    print_list('Carriers', codes)

    codes = options(soup, 'AirportList')
    print_list('Airports', codes)

main()
