import os
from pathlib import Path
import pandas as pd


DIR = r'D:\script\Python-Learning\FileHandling\Excel'
excelFile = os.path.join(DIR, 'WikiCitation.xlsx')
wikifile = os.path.join(DIR, 'UrWikiArticle.txt')
outfile = os.path.join(DIR, 'output.txt')

data = pd.read_excel(excelFile)
df = pd.DataFrame(
    data, columns=['RefNum', 'Title', 'URL', 'Date', 'WEB', 'AccDate'])

startRef = '<ref>{{cite web'
endRef = '}} </ref>'
p = '|'
w = 'و'

refDict = {}


def refDictionary():
    for idx, row in df.iterrows():
        keyCol = w + str(row['RefNum']) + w
        title = p + 'title=' + row['Title']
        url = p + 'URL=' + row['URL']
        web = p + 'website=' + row['WEB']
        date = p + 'date=' + str(row['Date'])
        accessdate = p + 'access-date=' + str(row['AccDate'])
        ref = startRef + title + url + web + date + accessdate + endRef

        refDict[keyCol] = ref

    return refDict


dlinks = refDictionary()

wikitext = Path(wikifile).read_text(encoding='utf-8')

for r in tuple(refDict.items()):
    wikitext = wikitext.replace(*r)

with open(outfile, 'w', encoding='utf-8') as outfile:
    outfile.write(wikitext)
