import csv

def read_csv(openfile):
    csvdata = csv.reader(openfile, delimiter=',', quotechar='"')
    data = [i for i in csvdata]
    return data