from pathlib import Path
import csv
from csv import DictReader

BASE = Path('C:\LEARNING\MISC\Wikipedia')

nl = '\n'
s = " "
c = ' ،'
ds = "۔ "
btag = "'''"
NA = 'غیرموجود'
ls = "* "
title = ''
d = {}

def enURTransliterate():
    csvfile = BASE / 'EN_UR_CRIC.csv'

    with open(csvfile, encoding='utf-8') as cfile:
        csv_reader = csv.reader(cfile)
        for row in csv_reader:
            d[row[0]] = row[1]

    return d


# Get dictionary of English roman words and Urdu Words
en_ur_dict = enURTransliterate()

youngAgeCric = d['unho']+s+d['nay']+s+d['choti']+s+d['umar']+s+d['mein']+s+d['maqami']+s+d['cric']+s+d['ka']+s+d['aghaaz']+s+d['kar']+s+d['diya']+s+d['tha']+c

club_firstcric = d['iss']+s+d['ke']+s+d['baad']+s+d['wo']+s+d['mukhtalif']+s+d['clubo']+s+d['ki']+s+d['taraf']+s+ d['se']+s+d['khailti']+s+d['rahein']+s+d['aur']+s+d['first']+s+d['class']+s+d['cric']+s+d['bhi']+s+d['khaili']+ds

print(youngAgeCric)
print(club_firstcric)