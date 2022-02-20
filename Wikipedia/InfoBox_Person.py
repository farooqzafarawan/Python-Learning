from pprint import pprint
import pywikibot
from gooey import Gooey
from gooey import GooeyParser
import argparse
import csv
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

s = ' '
d = {}


def enURTransliterate():
    BASE = Path(r'D:\script\Python-Learning\FileHandling\CSV')
    csvfile = BASE / 'ENG_UR.csv'

    with open(csvfile, encoding='utf-8') as cfile:
        csv_reader = csv.reader(cfile, delimiter=',')
        for row in csv_reader:
            d[row[0]] = row[1]


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
        if info.get(key, 'NA'):
            
            if d.get(val,'NF'):
                infoBox += nl + p + key + espc + d[val]

    briefUrduInfo = f'''
        | honorific_prefix   = {info['honorific_prefix']}
        | name               = {info['name']}
        | image              = 
        | alt                = 
        | caption            = {info['caption']}
        | native_name        = 
        | birth_name         = 
        '''

    infoBox += infoClose

    return infoBox


#@Gooey(progress_regex=r"^progress: (\d+)%$")
def main():
    # parser = GooeyParser(description="Add Infobox")
    # parser = argparse.ArgumentParser()

    # parser.add_argument('-t', '--title', required=True, help='Enter Title Name')
    # parser.add_argument('-l', '--lang', choices=['en', 'ar'], help='Select Language', default='en')
    # args = parser.parse_args()
    # title = args.title
    # langArg = args.lang

    title = 'Anita Ayoob'
    langArg ='en'
    # Get page based on title and language supplied as arguments
    page = getWikiPage(langArg, title)

    # POpulate interwiki language dictionary to get page title in other langs
    interDict = populateInterwiki(page, 'ur')

    # Get all templates including Infobox template
    all_templates = page.raw_extracted_templates

    # Get just Infobox template as a dictionary
    InfoDict = extractInfoTemplate(all_templates)

    # Get Infobox for Urdu Page with required params
    urInfoBox = UrduInfoBox(InfoDict)

    # Add Urdu Infobox before page text
    urTitle = interDict['ur']
    urpage = getWikiPage('ur', urTitle )
    urpage.text = urInfoBox + '\n\n' + urpage.text

    urpage.save(summary='اضافہ خانہ معلومات', minor=False)


if __name__ == "__main__":
    main()
