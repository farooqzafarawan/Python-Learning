import csv
import os
import datetime
import time
import re
import requests
import pywikibot
import mwparserfromhell as mwp
from bs4 import BeautifulSoup
import soupsieve as sv
from pathlib import Path

BASE = Path(r'E:\Python-Learning\FileHandling\CSV')
csvfile = BASE / 'ENG_UR.csv'

page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.content, 'html.parser')

covid19_day = soup.find(id="main_table_countries_today")
table = soup.find("table", id="main_table_countries_today")

s = ' '
nl = '\n'
d = {}


def enURTransliterate():
    with open(csvfile, encoding='utf-8') as cfile:
        csv_reader = csv.reader(cfile, delimiter=',')
        for row in csv_reader:
            d[row[0]] = row[1]


def table_header():
    theader = table.findAll('thead')
    header_titles = theader[0].text
    t_header = [title for title in header_titles.split('\n') if title != ""]
    t_header[0] = 'Num'
    t_header[1] = 'Country'
    t_header[7] = 'NewRecovered'
    t_header[9] = 'Serious'
    t_header[10] = 'TotalCases/1M Pop'
    t_header[13] = 'Tests/1M pop'
    t_header[14] = 'Population'
    t_header[15] = 'Continent'
    t_header.append('Extra18')
    t_header.append('Extra19')
    t_header.append('Extra20')
    t_header.append('Extra21')

    print(t_header)

    return t_header


t_header = table_header()


def covid_cases_country():
    d_covid19 = {}
    cnt_country = 0

    classToIgnore = ["total_row_world", "row_continent"]
    rows = sv.select('tr:not(.total_row_world, .row_continent)', table)

    #rows = table.find_all("tr", class_=lambda x: x not in classToIgnore)
    #rows = filter(lambda row: not row.find(class_='total_row_world'), rows)
    #data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
    continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

    for i, tr in enumerate(rows):
        dict_day = {}

        if i == 0:
            continue

        for tdcnt, td in enumerate(tr.findAll("td")):
            data = td.findChildren(text=True)
            dict_day[t_header[tdcnt]] = td.text
            #tdcnt += 1

        if 'Country' in dict_day:
            d_covid19[dict_day['Country']] = dict_day
            cnt_country += 1

        # Getting data of first 36 countries (38 -2 )
        if cnt_country >= 88:
            break

    return d_covid19


covid_cases = covid_cases_country()

# for d in covid_cases:
#     print(d)


def output_results():
    import datetime
    now = datetime.datetime.now()

    dirpath = r'D:\Wikipedia\code_output'

    dayadd = datetime.datetime.strftime(datetime.datetime.now(), '%d%b%Y_%H%M')
    csvfile_name = 'covid_cases_' + str(dayadd) + '.csv'
    # csv file for writing new records
    csvfile = os.path.join(dirpath, csvfile_name)

    with open(csvfile, mode='w', newline='') as csvwrite:
        t_head = ['Region', 'TotalCases', 'NewCases', 'TotalDeaths',
                  'NewDeaths', 'TotalRecovered', 'ActiveCases', 'TotalTests']
        line_written = 0

        writer = csv.writer(csvwrite, delimiter=';')

        writer.writerow(t_head)
        for d in covid_cases:
            row_fields = [covid_cases[d]['Country'], covid_cases[d]['TotalCases'], covid_cases.get(d, {}).get('NewCases', 'NA'), covid_cases[d]['TotalDeaths'], covid_cases.get(d, {}).get('NewDeaths', 'NA'), covid_cases[d]['TotalRecovered'], covid_cases[d]['ActiveCases'], covid_cases.get(d, {}).get('TotalTests', 'NA')
                          ]

            writer.writerow(row_fields)
            line_written += 1

    return line_written


covid_recs = output_results()

print(covid_recs)


def write_output(newtext, day_update, filename):
    baseDir = r'D:\Wikipedia\code_output'
    newfile = os.path.join(baseDir, filename)

    with open(newfile, 'a', encoding='utf8') as fout:
        fout.write(day_update)


def msg_start_date():
    now = datetime.datetime.now()

    #month = now.month
    d_UrduMonth = {
        1: 'جنوری',
        2: 'فروری',
        3: 'مارچ',
        4: 'اپریل',
        5: 'مئی',
        6: 'جون',
        7: 'جولائی',
        8: 'اگست',
        9: 'ستمبر',
        10: 'اکتوبر',
        11: 'نومبر',
        12: 'دسمبر'
    }

    covid_mon = d_UrduMonth[now.month]
    day_mon = f'*  {now.day} ' + covid_mon
    final_date = day_mon + s + str(now.year) + ': '

    return final_date


def coronaDailyUpdate(country):
    #now = datetime.datetime.now()

    covid = covid_cases[country]
    TotCases = covid['TotalCases']
    TotDeaths = covid['TotalDeaths']
    NewDeaths = covid['NewDeaths']
    TotRecover = covid['TotalRecovered']
    ActCases = covid['ActiveCases']
    NewCases = covid['NewCases']
    TotTests = covid['TotalTests']
    #NewTests    = pk_covid['NewTests']

    msg_date = msg_start_date()

    DailyUpd = f'''{d['youmia']} {d['amwaat']} {NewDeaths}، '''
    DailyUpd += f'''{d['kul']} {d['amwaat']} {TotDeaths}، '''
    DailyUpd += f'''{d['kul']} {d['case']} {TotCases}، '''
    DailyUpd += f'''{d['naye']} {d['case']} {NewCases}، '''
    DailyUpd += f'''{d['kul']} {d['test']} {TotTests}، '''
    DailyUpd += f'''{d['kul']} {d['sehatyaab']} {TotRecover}، '''
    DailyUpd += f'''{d['zair elaaj']} {ActCases} '''

    day_update = msg_date + DailyUpd + nl + nl

    return day_update


def wikiTextReplace(wikicode, day_update, country):
    #wikicode = mwp.parse(wikitext)
    sections = wikicode.get_sections()
    cntSection = len(sections)

    for i, section in enumerate(wikicode.get_sections(include_headings=True)):
        clean = section.strip_code()
        secHeading = section.filter_headings()
        secText = section.filter_text()
        if i == cntSection - 2:
            insSection = section.append(day_update)

    # regex = r"((. |\n)*)(==.*حوالہ جات.*==)"

    # subst = f"\\1{day_update}\\n\\n\\3"
    # # change wikitext to wikicode
    # replacedText = re.sub(regex, subst, str(wikicode), 0)

    replacedText = str(wikicode)
    write_output(replacedText, day_update, f'{country}_corona_epidemic.txt')

    return replacedText


def wiki_stats(wikiSave, cntry, cntry_wikiLink):
    day_update = coronaDailyUpdate(cntry)

    title = cntry_wikiLink
    site = pywikibot.Site('ur', 'wikipedia')
    urpage = pywikibot.Page(site, title)

    wikitext = urpage.get()
    wikicode = mwp.parse(wikitext)

    result = wikiTextReplace(wikicode, day_update, cntry)
    urpage.text = result

    if wikiSave:
        urpage.save(summary='خودکار: اندراج معلومات ', minor=False)


def Pak_stats(wikiSave):
    day_update = coronaDailyUpdate('Pakistan')

    title = 'پاکستان_میں_کورونا_وائرس_کی_وبا،_2020ء'
    site = pywikibot.Site('ur', 'wikipedia')
    urpage = pywikibot.Page(site, title)

    wikitext = urpage.get()
    wikicode = mwp.parse(wikitext)

    result = wikiTextReplace(wikicode, day_update, 'PK')

    urpage.text = result

    if wikiSave:
        urpage.save(summary='خودکار: اندراج معلومات ', minor=False)

    # return day_update


def mainStats(wikiSave):
    cntry_link = {
        'USA': 'امریکا میں کورونا وائرس کی وبا، 2020ء',
        'Pakistan': 'پاکستان میں کورونا وائرس کی وبا',
        'India': 'بھارت میں کورونا وائرس کی وبا',
        'Italy': 'اطالیہ میں کورونا وائرس کی وبا',
        'Brazil': 'برازیل میں کورونا وائرس کی وبا'
    }

    
    for cntry in cntry_link:
        try:
            wiki_stats(wikiSave, cntry, cntry_link[cntry])
            time.sleep(6)
        except Exception as e:
            print(e)
            continue

wikiSave = True

enURTransliterate()

mainStats(wikiSave)
# usa_stats(wikiSave)
# Pak_stats(wikiSave)
