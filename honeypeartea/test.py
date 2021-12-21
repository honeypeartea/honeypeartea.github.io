import os, csv
from numpy import genfromtxt
import pprint

def csv2list(csvpath):
    with open(csvpath, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def main():
    college = 'Davis'
    year = 2014
    category = 'race'

    if category == 'race':
        data = csv2list('../static/race.csv')
        dict = {
            'Asian': 0,
            'White': 0,
            'Hispanic/ Latino': 0,
            'African American': 0,
            'American Indian': 0
        }

        for row in data:
            for race in dict.keys():
                if row[2] == college and row[3] == race and row[7] == str(year):
                    dict[race] += float(row[6])

        reminder = 100 - sum(dict.values())
        print(reminder)

        pprint.pprint(dict)
if __name__ == '__main__':
    main()
