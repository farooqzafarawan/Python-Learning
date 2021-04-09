import csv
import os
from pathlib import Path

dirpath = r'D:\script\Python-Learning\FileHandling\CSV'
infile = os.path.join(dirpath, 'Wiki.csv')
outfile = os.path.join(dirpath, 'output.txt')
wikifile = os.path.join(dirpath, 'mowasha.txt')

startRef = '<ref>{{cite web'
endRef = '}} </ref>'
p = '|'

refDict = {}


def refDictionary():
    with open(infile, encoding='utf-8') as csvFile:
        reader = csv.DictReader(csvFile,  delimiter='\t')
        print(reader.fieldnames)
        keyCol = reader.fieldnames[0]
        for row in reader:
            aDate = p + row['AccessDate']
            title = p + row['Title']
            url = p + row['URL']
            date = p + row['Date']
            ref = startRef + title + url + aDate + date + endRef

            refDict[row[keyCol]] = ref

        # return refDict


wikitext = Path(wikifile).read_text(encoding='utf-8')

print(wikitext)

dlinks = refDictionary()

for r in tuple(refDict.items()):
    wikitext = wikitext.replace(*r)

# for r in tuple(dlinks.items()):
#     wikitext = wikitext.replace(*r)

print(wikitext)

with open(outfile, 'w', encoding='utf-8') as outfile:
    outfile.write(wikitext)

# <ref>{{cite web 
# |url = https: // www.youtube.com/watch?v = pBBQQ6dGhGc
# |title = Overload _ Pichal Pairee(Witch) - Pakistani Band
# |author = 
# |date = 3 مارچ 2021
# |website = Youtube
# }} < /ref >
