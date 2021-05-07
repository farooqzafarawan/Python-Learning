# Substituting text in a field by looking up in a dictionary
from collections import OrderedDict

info = OrderedDict([('name', 'Anita Ayoob'),
                    ('birth_name', ''),
                    ('birth_date', ''),
                    ('birth_place', ''),
                    ('nationality', 'Pakistani'),
                    ('other_names', 'Aneeta Ayoob, Anita Ayub, Anita Ayub Majeed'),
                    ('occupation', 'Actress'),
                    ('television', ''),
                    ('title', ''),
                    ('spouse', 'Saumil Patel'),
                    ('partner', ''),
                    ('children', 'Shezap'),
                    ('relatives', ''),
                    ('family', 'Amber Ayub (sister)'),
                    ('signature', ''),
                    ('footnotes', '')])

d = {'anita': 'انیتا',
     'aneeta': 'انیتا',
     'ayub': 'ایوب',
     'ayoob': 'ایوب',
     'amber': 'عنبر',
     'saumil': 'سومل',
     '(sister)': '(بہن)',
     'patel': 'پٹیل',
     'shezap': 'شیزپ',
     'pakistani': 'پاکستانی'
     }


def getValTrans(multiVal):
    fullStr = ''
    urcoma = '،'
    if ',' in multiVal:
        newVal = multiVal.lower().split(',')
        for valA in newVal:
            valB = valA.split()
            str1 = ''
            for val in valB:
                str1 += d.get(val, val) + s
            fullStr += str1 + urcoma
        fullStr = fullStr.rstrip(urcoma)
    else:
        newVal = multiVal.lower().split()
        for val in newVal:
            fullStr += d.get(val, val) + s

    return fullStr


infoBox = ''
nl = '\n'
p = '| '
espc = ' = '
s = ' '

for key, val in info.items():
        if info.get(key, 'NA'):
            enVal = getValTrans(val)
            infoBox += nl + p + key + espc + enVal

print(infoBox)
