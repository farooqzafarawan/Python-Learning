#Read CSV file containing different fields delimited by comma
import os
import csv

## sample.csv
# ID,CustID,Name,Email,Phone,Zip,City,State,Country,Address
# 1,2323651,Ferguson,Abcush9761@gmail.com,(716) 594 7675,33182,MIAMI,FL,US,123 JOFFRA DR

dirpath = r'D:\MISC'
csvfile = os.path.join(dirpath,'sample.csv')

with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Print the header row')
            print(row)
        else:
            print(row)
        line_count += 1
