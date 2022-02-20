import mwparserfromhell as mwp
import re
from mwparserfromhell.smart_list import SmartList
from pathlib import Path

BASE_DIR = Path('PLACEHOLDER DIR')
infile = 'انیٹ فیلوز.txt'
wikifile = BASE_DIR / infile

with open(wikifile, encoding='utf-8') as f:
    wikitext = f.read()

wikicode = mwp.parse(wikitext)
smartWiki = SmartList(wikicode)

refHeading = 'حوالہ جات'
testHeading = 'ٹیسٹ کیریئر'
headings = wikicode.filter_headings()

# if heading.title == testHeading
filtered_headings = [heading.title.strip() for heading in headings]

plain_text = ''
for node in wikicode.nodes:
    type_of_node = type(node)
    if type_of_node == mwp.nodes.template.Template:
        continue
    if type_of_node == mwp.nodes.argument.Argument:
        continue
    if type_of_node != mwp.nodes.text.Text:
        if type(node) == mwp.nodes.tag.Tag:
            str_node = node.contents
        elif type(node) == mwp.nodes.external_link.ExternalLink:
            str_node = node.title
        elif type(node) == mwp.nodes.heading.Heading:
            str_node = node.title
        elif type(node) == mwp.nodes.wikilink.Wikilink:
            str_node = node.title
        plain_text += str(str_node)
    else:
        plain_text += str(node)


#testNode = wikicode.nodes.index(filtered_headings[1]) + 1

for i, section in enumerate(wikicode.get_sections()):
    clean = section.strip_code()
    header = headings[i]
    if header.title == refHeading:
        print('Inside References')

print(wikicode)

# regex = r"((. |\n)*)(==.*حوالہ جات.*==)"
# subst = f"\\1{day_update}\\n\\n\\3"
# replacedText = re.sub(regex, subst, wikicode, 0)
