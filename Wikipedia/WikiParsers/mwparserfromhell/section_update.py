from pathlib import Path
#from mwparserfromhell.nodes import Argument, Heading, Template, Text
import mwparserfromhell as mwp


def write_output(newtext, filename):
    outDir = Path(r'D:\Wikipedia\code_output')
    newfile = outDir / filename

    with open(newfile, 'w', encoding='utf8') as fout:
        fout.write(str(newtext))

BASE_DIR = Path(r'D:\script\MohibPython\DATA')
infile = 'انیٹ فیلوز.txt'
wikifile = BASE_DIR / infile

refHeading = 'حوالہ جات'
testHeading = 'ٹیسٹ کیریئر'

with open(wikifile, encoding='utf-8') as f:
    wikitext = f.read()

wikicode = mwp.parse(wikitext)
sections = wikicode.get_sections()
cntSection = len(sections)

for i, section in enumerate(wikicode.get_sections(include_headings=True)):
    clean = section.strip_code()
    secHeading = section.filter_headings()
    secText = section.filter_text()
    if i == cntSection-2:
        wikiAdd = "اب کیا لکھیں دو لائن کے بعد" + nl
        wikiAdd += "just adding one mnore row" + nl + nl
        #sectionUpdText = str(secText[0]) + str(secText[1]) + wikiAdd
        insSection = section.append(wikiAdd)
        #UpdSection = wikicode.replace(section, secText)
