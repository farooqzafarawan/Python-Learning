import json
from pathlib import Path

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

jsonfile = BASE / 'output_template.json'
with open(jsonfile, 'r') as read_file:
    infoBoxActor = json.loads(read_file.read())

for item in infoBoxActor:
    print(f'{item} => {infoBoxActor[item]}')
