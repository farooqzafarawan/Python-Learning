from pathlib import Path
from mwparserfromhell.nodes import Argument, Heading, Template, Text
import mwparserfromhell as mwp

code = mwp.parse("Here is {{aaa|{{bbb|xyz{{ccc}}}}}} and a [[page|link]]")
tmpl1, tmpl2, tmpl3 = code.filter_templates()
tmpl4 = mwp.parse("{{ccc}}").filter_templates()[0]

BASE_DIR = Path(r'D:\script\MohibPython\DATA')
infile = 'انیٹ فیلوز.txt'
wikifile = BASE_DIR / infile

with open(wikifile, encoding='utf-8') as f:
    wikitext = f.read()


def write_output(newtext, filename):
    import time
    import os
    baseDir = r'D:\Wikipedia\code_output'
    newfile = os.path.join(baseDir, filename)

    with open(newfile, 'w', encoding='utf8') as fout:
        #print('Printing appended Urdu Page', time.ctime(), file=fout)
        #print(newtext, file=fout)
        fout.write(str(newtext))


#refTag = '<ref>{{cite web|title=انیٹ فیلوز|URL=https://www.espncricinfo.com/australia/content/player/53500.html|website=cricinfo|date=27 مارچ 2021}} </ref>'
wikicode = mwp.parse(wikitext)
refHeading = 'حوالہ جات'
testHeading = 'ٹیسٹ کیریئر'

templates = {}
i = 1
headings = wikicode.filter_headings()
for template in wikicode.filter_templates():
    tplName = str(template.name).strip()
    if tplName == 'cite web':
        citeweb = tplName+str(i)
        templates[citeweb] = str(template)
        i += 1

    templates[tplName] = str(template)
    if template.name == refHeading:
        print(template.name)

templates = wikicode.filter_templates()
for template in wikicode.filter_templates():
    if template.name.matches("cite web"):
        if not template.has("date"):
            template.add("date", "16 اپریل 2021")
        elif not template.has("accessdate"):
            template.add("accessdate", "17 April 2021")
        elif template.has("accessdate"):
            origTemplate = template
            template.get('accessdate').value = '17 February 2022'
            templates.append(template)
            print(template)
            #wikicode = wikicode.replace(origTemplate, template )

    if template.name == 'cite web':
        print('WEB Reference')

headcnt = 0
sections = {}
nl = '\n'

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
        insSection = section.append( wikiAdd)
        #UpdSection = wikicode.replace(section, secText)

    if i < len(headings):
        header = str(headings[i]).strip()

    sections[headcnt] = section
    if header.title == refHeading:
        headcnt -= 1
        print('Inside References')

    headcnt += 1

write_output(wikicode, 'WikiUpdatedText.txt')
# print(wikicode)

# cricplayer = wikicode.filter_templates()[2]
# for param in cricplayer.params:
#     print(param)
