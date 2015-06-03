import csv
import pprint

fieldname = "wgs84_pos#lat"
minval = -90
maxval = 90


def skip_lines(input_file, skil):
    for i in range(0, skip):
        next(input_file)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def audit_float_field(v, counts):
    v = v.strip()
    if v == "NULL":
        counts['nulls'] += 1
    elif v == "":
        counts['empties'] += 1
    elif is_array(v):
        counts['arrays'] += 1
    elif not is_number(v):
        print "Found non number:",v
    else:
        v = float(v)
        if not ((minval < v) and (v < maxval)):
            print "Found out of range value:", v

if __name__ == "__main__":
    input_file = csv.DictReader(open("cities3.csv"))
    skip_lines(input_file, 3)
    counts = {"nulls": 0, "empties":0 , "arrays":0}
    nrows = 0
    for row in input_file:
        audit_float_field(row[fieldname], counts)
        nrows += 1
    print "num cities:", nrows
    print "nulls:", counts['nulls']
    print "empties:", counts['empties']
            
