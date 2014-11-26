import nltk
import csv

with open('metromanila.csv') as MMCSV:
    MMReader = csv.reader(MMCSV, delimiter = ',')
    for row in MMReader:
        print(row)
