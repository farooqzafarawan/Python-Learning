import mwparserfromhell as mwp
from pathlib import Path

BASE_DIR = Path(r'D:\script\MohibPython\DATA')
infile = 'انیٹ فیلوز.txt'
wikifile = BASE_DIR / infile

with open(wikifile, encoding='utf-8') as f:
    wikitext = f.read()

wikicode = mwp.parse(wikitext)

tags = []

for tag in wikicode.filter_tags(matches=lambda tag: tag.tag == "ref"):
        tags.append(tag)

for tag in tags:
    print(tag)
