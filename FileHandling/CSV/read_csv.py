import os
import csv

## sample.csv
# ID,MergeID,CustomerNo,FirstName,LastName,Email,Phone,Zip,City,State,Country,ShippingAddress,isActive
# 1,0,2323651,Ferguson,Chen F.,Abcush9761@gmail.com,(716) 594 7675,33182,MIAMI,FL,US,123 JOFFRA DR,1

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
