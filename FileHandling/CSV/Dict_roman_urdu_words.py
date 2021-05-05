import csv
#import os
from pathlib import Path

BASE = Path('D:\script\Python-Learning\FileHandling\CSV')
csvfile = BASE / 'ENG_UR.csv'

d = {}
def enURTransliterate():
    with open(csvfile, encoding='utf-8') as cfile:
        csv_reader = csv.reader(cfile, delimiter=',' )
        line_count = 0
        for row in csv_reader:
            d[row[0]] = row[1]

NewCases = 10
TotCases = 1200
NewDeaths = 90
TotDeaths = 190
ActCases = 149
TotTests = 1000
TotRecover = 1100
s = ' '

DailyUpd = f'''{d['youmia']} {d['amwaat']} {NewDeaths}، '''
DailyUpd = f'''{d['kul']} {d['amwaat']} {TotDeaths}، '''
DailyUpd += f'''{d['kul']} {d['case']} {TotCases}، '''
DailyUpd += f'''{d['naye']} {d['case']} {NewCases}، '''
DailyUpd += f'''{d['kul']} {d['test']} {TotTests}، '''
DailyUpd += f'''{d['kul']} {d['sehatyaab']} {TotRecover}، '''
DailyUpd += f'''{d['zair elaaj']} {ActCases}، '''

print(DailyUpd)


