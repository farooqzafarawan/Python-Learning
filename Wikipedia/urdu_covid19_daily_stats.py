import csv
import os
import datetime
import re
import requests
import pywikibot
import mwparserfromhell as mwp
from bs4 import BeautifulSoup

page = requests.get(
    "https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.content, 'html.parser')

print('Testing')

covid19_day = soup.find(id="main_table_countries_today")

table = soup.find("table", id="main_table_countries_today")


def table_header():
    theader = table.findAll('thead')
    header_titles = theader[0].text
    t_header = [title for title in header_titles.split('\n') if title != ""]
    t_header[0] = 'Country'
    t_header[7] = 'Serious'
    t_header[11] = 'NewTests'
    print(header_titles)

    return t_header


t_header = table_header()


def covid_cases_country():
    d_covid19 = {}
    cnt_country = 0

    rows = table.findAll('tr')
    #data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

    for tr in rows:
        dict_day = {}
        i = 0
        for td in tr.findAll("td"):
            data = td.findChildren(text=True)
            if data:
                dict_day[t_header[i]] = data[0]
            i += 1

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


def write_output(newtext, filename):
    baseDir = r'D:\Wikipedia\code_output'
    newfile = os.path.join(baseDir, filename)

    with open(newfile, 'w', encoding='utf8') as fout:
        fout.write(newtext)


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
    final_date = f'* {now.day} {covid_mon} {now.year} : '

    return final_date


def usa_stats():
    now = datetime.datetime.now()

    usa_covid = covid_cases['USA']
    TotCases = usa_covid['TotalCases']
    TotDeaths = usa_covid['TotalDeaths']
    NewDeaths = usa_covid['NewDeaths']
    TotRecovered = usa_covid['TotalRecovered']
    ActCases = usa_covid['ActiveCases']
    NewCases = usa_covid['NewCases']
    #NewTests = usa_covid['NewTests']
    TotTests = usa_covid['TotalTests']

    msg_date = msg_start_date()
    day_update = f' {NewCases} نئے کیس ، {TotCases} کل کیس ، {NewDeaths} یومیہ اموات ، {TotDeaths} کل اموات ، {ActCases} زیر علاج ،  {TotRecovered} کل صحتیاب ، {TotTests} کل ٹیسٹ'
    day_update = msg_date + day_update

    title = 'امریکا میں کورونا وائرس کی وبا، 2020ء'
    site = pywikibot.Site('ur', 'wikipedia')
    urpage = pywikibot.Page(site, title)

    wikitext = urpage.get()
    wikicode = mwp.parse(wikitext)

    for section in wikicode.get_sections(levels=[3]):
        clean = section.strip_code()

    for section in wikicode.get_sections(levels=[4]):
        sec_4 = section
        #upd_section = sec_4 + '\n' + day_update
        print(sec_4)

    regex = r"((. |\n)*)(==.*حوالہ جات.*==)"

    subst = f"\\1{day_update}\\n\\n\\3"
    result = re.sub(regex, subst, wikitext, 0)

    write_output(result, 'us_corona_epidemic.txt')

    urpage.text = result
    # save the page
    urpage.save(summary='خودکار: اندراج ', minor=False)

    print(wikicode)

    return day_update


def Pak_stats():
    now = datetime.datetime.now()

    usa_covid = covid_cases['Pakistan']
    TotCases = usa_covid['TotalCases']
    TotDeaths = usa_covid['TotalDeaths']
    NewDeaths = usa_covid['NewDeaths']
    TotRecovered = usa_covid['TotalRecovered']
    ActCases = usa_covid['ActiveCases']
    NewCases = usa_covid['NewCases']
    #NewTests = usa_covid['NewTests']
    TotTests = usa_covid['TotalTests']

    msg_date = msg_start_date()
    day_update = f' {NewCases} نئے کیس ، {TotCases} کل کیس ، {NewDeaths} یومیہ اموات ، {TotDeaths} کل اموات ، {ActCases} زیر علاج ،  {TotRecovered} کل صحتیاب ، {TotTests} کل ٹیسٹ'
    day_update = msg_date + day_update

    title = 'پاکستان_میں_کورونا_وائرس_کی_وبا،_2020ء'
    site = pywikibot.Site('ur', 'wikipedia')
    urpage = pywikibot.Page(site, title)

    wikitext = urpage.get()
    wikicode = mwp.parse(wikitext)

    for section in wikicode.get_sections(levels=[3]):
        clean = section.strip_code()

    for section in wikicode.get_sections(levels=[4]):
        sec_4 = section
        #upd_section = sec_4 + '\n' + day_update
        print(sec_4)

    regex = r"((. |\n)*)(==.*حوالہ جات.*==)"

    subst = f"\\1{day_update}\\n\\n\\3"
    result = re.sub(regex, subst, wikitext, 0)

    write_output(result, 'Pak_corona_epidemic.txt')

    urpage.text = result
    # save the page
    urpage.save(summary='خودکار: اندراج ', minor=False)

    print(wikicode)

    return day_update


ur_day = usa_stats()
pk_corona_stats = Pak_stats()

print(ur_day)
