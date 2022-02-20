#import wikitextparser as wtp
import mwparserfromhell as mwp
import pywikibot 
import os

BASEDIR = r'<PLACEHOLDER PATH>'
FILENAME = 'AsimB.txt'
newfile = os.path.join(BASEDIR, FILENAME )

urpage = open(newfile,'r',encoding='utf-8').read()

wikitext = urpage
wikicode = mwp.parse(wikitext)

sections = wikicode.get_sections()

for section in sections:
    print(section)
