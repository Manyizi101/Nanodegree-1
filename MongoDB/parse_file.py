def parse_file(datafile):
    data= []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")
            entry = {}

            for i,value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1
    return data


# read csv files
import csv

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data


# read xls files
import xlrd
def parse_xls(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
             for col in range(sheet.ncols)]
                for r in range(sheet.nrows)]
    
