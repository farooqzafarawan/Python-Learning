import csv
import os

dirpath = r'D:\script\Python-Learning\FileHandling\CSV'
infile = os.path.join(dirpath, 'Wiki.csv')

refDict = {}
with open(infile, encoding='utf-8') as csvFile:
    reader = csv.DictReader(csvFile,  delimiter='\t')  
    print(reader.fieldnames)
    keyCol = reader.fieldnames[0] 
    for row in reader:
        print(row)
        refDict[row[keyCol]] = [row['AccessDate'], row['Title'], row['URL'],row['Date']]

startRef = '<ref>{{cite web'
endRef = '}} </ref>'
p = '|'
for key,value in refDict.items():
    accessDate = p + value[0]
    title = p + value[1]
    url = p + value[2]
    date = p + value[3]
    ref = startRef + accessDate + title + url + endRef 
    print(ref)


