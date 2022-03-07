from asyncore import write
from pprint import pprint
import pywikibot
from gooey import Gooey
from gooey import GooeyParser
import argparse
import csv
import json
from pathlib import Path

sample = f'''
    {{Infobox person
    | honorific_prefix   =
    | name               = Zara Noor Abbas
    | honorific_suffix   =
    | image              =
    | alt                =
    | caption            = Abbas in 2018
    | native_name        =
    | pronunciation      =
    | birth_name         =
    | birth_date         = {{birth date and age|1991|03|13|df=y}}
    | birth_place        = [[Lahore]], [[Punjab, Pakistan]]
    | nationality        = Pakistani
    | other_names        = 
    | citizenship        = 
    | education          = [[Beaconhouse National University]]
    | alma_mater         = 
    | occupation         = [[Actress]], [[Model (person)|Model]]
    | years_active       = 2016–present
    | known_for          = ''[[Dharkan (2016 TV series)|Dharkan]]'' (2016) <br/>''[[Khamoshi (TV series)|Khamoshi]]'' (2017) <br/> ''[[Ehd-e-Wafa]]'' (2019) <br/>''[[Parey Hut Love]]'' (2019)
    | notable_works      = 
    | home_town          = 
    | height             = 
    | weight             = 
    | spouse             = {{marriage|[[Asad Siddiqui]]|2017}}
    | partner            = 
    | relatives          = [[Asma Abbas]] (mother)<br/>[[Bushra Ansari]] (aunt)
    | awards             = 
    | website            = 
    }}
    '''

BASE = Path('<DIR>')

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

def inFileReader():
    csvfile = BASE / 'women_actress.csv'
    lstPlayers = []
    with open(csvfile, encoding='utf-8') as cfile:
        dcsv_reader = csv.DictReader(cfile, delimiter='|')

        # get column names ENG:URDU
        col = dcsv_reader.fieldnames

        for row in dcsv_reader:
            lstPlayers.append(row)

    return lstPlayers

def getWikiPage(lang, title):
    site = pywikibot.Site(lang, 'wikipedia')
    page = pywikibot.Page(site, title)

    return page


def populateInterwiki(page, langArg):
    langDict = {}
    langlst = page.iterlanglinks()

    for i in langlst:
        lang = str(i.site).split(':')[1]
        langDict[lang] = i.title
        if lang == langArg:
            return langDict
            break

    if len(langDict) == 0:
        import sys
        print('Link Dictionary is empty')
        sys.exit()


def extractInfoTemplate(all_templates):
    for tmpl, params in all_templates:
        if tmpl == 'short description':
            print('short description')
            pprint(params)
        elif tmpl == 'Infobox person':
            InfoDict = params
            pprint(params)
        elif tmpl == 'IMDb name':
            pprint(params)
        elif tmpl == 'Instagram':
            pprint(params)

    return InfoDict

def UrduInfoBox(info):
    infoStart = "{{ Infobox person"
    infoClose = "}}"

    infoBox = ''
    nl = '\n'
    p = '| '
    espc = ' = '
    # Peronal Info
    infoBox = f'''{infoStart}'''

    for key, val in info.items():
        val = info.get(key, 'NA')
        if val:
            print(key,"=>",val)
            #infoBox += nl + p + key + espc + d[val]

    briefUrduInfo = f'''
        | name               = {info['name']}
        | image              = 
        | alt                = 
        | caption            = {info['caption']}
        | native_name        = 
        | birth_name         = 
        '''

    infoBox += infoClose

    return infoBox

def write_output(newtext):
    newfile = BASE / 'output_template.json'
    with open(newfile, 'w', encoding='utf8') as fout:
        fout.write(json.dumps(newtext))

def write_templates(itemlist):
    newfile = BASE / 'output_template.txt'
    with open(newfile, 'w', encoding='utf8') as fout:
        fout.writeline("\n".join(str(item) for item in itemlist))

def intro():
    with open('file.json', 'r') as read_file:
        loaded_dictionaries = json.loads(read_file.read())

#@Gooey(progress_regex=r"^progress: (\d+)%$")
def getArticle(enTitle,urTitle):
    # parser = GooeyParser(description="Add Infobox")
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-t', '--title', required=True, help='Enter Title Name')
    # parser.add_argument('-l', '--lang', choices=['en', 'ar'], help='Select Language', default='en')
    # args = parser.parse_args()
    # title = args.title
    # langArg = args.lang

    
    # Get page based on title and language supplied as arguments
    page = getWikiPage("en", enTitle)

    # Populate interwiki language dictionary to get page title in other langs
    #interDict = populateInterwiki(page, 'ur')

    # Get all templates including Infobox template
    all_templates = page.raw_extracted_templates

    #write_templates(all_templates)   #templates are tuples of (str,orderedDict)

    # Get just Infobox template as a dictionary
    InfoDict = extractInfoTemplate(all_templates)

    write_output(InfoDict)
    
    # Get Infobox for Urdu Page with required params
    urInfoBox = UrduInfoBox(InfoDict)

    # Add Urdu Infobox before page text
    # urTitle = interDict['ur']
    # urpage = getWikiPage('ur', urTitle )
    # urpage.text = urInfoBox + '\n\n' + urpage.text

    #urpage.save(summary='اضافہ خانہ معلومات', minor=False)


if __name__ == "__main__":
    lstActorPerson = inFileReader()
    for player in lstActorPerson:
        engTitle = player.get('ENG')
        urTitle  = player.get('URDU')

        getArticle(engTitle,urTitle)    
        
