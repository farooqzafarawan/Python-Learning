import mwparserfromhell as mwp
from pathlib import Path

BASE_DIR = Path(r'D:\script\MohibPython\DATA')
infile = 'انیٹ فیلوز.txt'
wikifile = BASE_DIR / infile

with open(wikifile, encoding='utf-8') as f:
    wikitext = f.read()

wikicode = mwp.parse(wikitext)

headings = wikicode.filter_headings()
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

print(plain_text)
