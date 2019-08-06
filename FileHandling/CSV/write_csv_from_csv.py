# Write selected fields from a CSV file in another CSV file

import csv
import os

# CSV File Format
# CustomerID,FirstName,LastName,Email,Phone
# 2323651,Pilar,Adam,abbeyh91@gmail.com,516 594 7675

dirpath = r'D:\Demo Data'
# Existing csv file containing data
csvfile = os.path.join(dirpath,'test.csv')

# csv file for writing new records
csvwritef = os.path.join(dirpath,'newfile.csv') 

with open(csvwritef, mode='w') as csvwrite, open(csvfile) as csvf:
    fieldnames = ['CustID','empFirstName', 'empLastName']
    writer = csv.writer(csvwrite)

    #csv_reader = csv.reader(csvf, delimiter=',')

    for row in csvf:
        
        rec = list(row.split(','))
        writer.writerow([rec[2], rec[3]])
