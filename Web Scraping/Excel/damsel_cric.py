import os
#from pathlib import Path
import pandas as pd
from pywikibot.page import Page
import pywikibot
import argparse
import time

DIR = r'C:\script\Python\DATA'
excelFile = os.path.join(DIR, 'WomenCricketer.xlsx')

nl = '\n'
s = " "
btag = "'''"
ref = '== حوالہ جات ==' + nl + '{{حوالہ جات}}'
NA = 'غیرموجود'
title = ''


def infoBox(title, row, T20):
    cricinfoREF = ''
    infoStart = "{{ Infobox cricketer"
    infoClosing = "}}"

    # ODI Info
    fmatch = row['First']
    lmatch = row['Last']
    tmatch = row['Mat']
    odi_runs = row['Runs']
    HS = row['HS']
    avg = row['Avg']
    wkt = row['WKT']
    #BestBowl = row['BBM']
    BowlAvg = row['BAvg']
    w5 = row['WI5']
    ct = row['Cat']
    st = row['ST']
    batS = row['BAT']
    bowlStyle = row['BOWL']
    ODEB_CNTRY = row['ODEB']
    # Peronal Info
    bd = row['Bday']
    if bd != NA:
        D, M, YR = bd.split('-')
    else:
        D, M, YR = 'NIL'

    city = row['City']
    Role_in_Team = row['Role']
    country = row['CNTRY']

    bday_temp = "{{Birth date and age |" + \
        YR + "|" + M + "|" + D + "| df = yes}}"

    # TEST or T20 info in same columns
    TDEB_YR = row['TFirst']
    TDEB = row['TDEB']
    TMATCH = row['TMat']
    TWICKETS = row['TWKT']
    TRUNS = row['TRUN']
    THS = row['THS']
    T50 = row['T50']
    T100 = row['T100']
    TCT = row['TCT']
    ST = 0

    infoBox = ''
    info1 = f'''{infoStart}
    | name = {title}
    | female = true
    | image =
    | country = {country} 
    | fullname = {title}
    | nickname = 
    | birth_date = {bday_temp}
    | birth_place = {city} {country}
    | heightft = 
    | heightinch = 
    | batting = {batS}
    | bowling = {bowlStyle}
    | role = {Role_in_Team}
    | international = true
    '''

    infoTest = f'''
    | testdebutdate =  
    | testdebutyear = {TDEB_YR}
    | testdebutagainst = {TDEB}'''
    infoT20 = f'''
    | T20Idebutdate =  
    | T20Idebutyear = {TDEB_YR}
    | T20Idebutagainst = {TDEB}'''
    infoODI = f'''
    | odidebutdate =
    | odidebutyear = {fmatch}
    | odidebutagainst = {ODEB_CNTRY}
    | odicap =

    | columns = 2
    '''

    infoTestHead = f'''[[خواتین ٹیسٹ کرکٹ|ٹیسٹ]]'''
    infoT20Head = f'''[[خواتین ٹی ٹوئنٹی انٹرنیشنل (WT20I)|ٹی ٹوئنٹی]]'''
    if T20 == 'Y':
        infoHeadDet = infoT20Head
    else:
        infoHeadDet = infoTestHead

    infoT20TestDet = f'''
    | column1 = {infoHeadDet}
    | matches1 = {TMATCH}
    | runs1 = {TRUNS}
    | bat avg1 = {row['TAV']}
    | 100s/50s1 = {T100}/{T50}
    | top score1 = {THS}
    | deliveries1 = {row['TBall']}
    | wickets1 = {row['TWKT']}
    | bowl avg1 = {row['TBAv']}
    | fivefor1 = -
    | tenfor1 = -
    | best bowling1 = -
    | catches/stumpings1 = {ST}/{TCT}
    '''

    infoODIDet = f'''
    | column2 = [[خواتین ایک روزہ بین الاقوامی|ایک روزہ]]
    | matches2 = {tmatch}
    | runs2 = {odi_runs}
    | bat avg2 = {avg}
    | 100s/50s2 = {row['CENT']}/{row['Fifty']}
    | top score2 = {HS}
    | deliveries2 = {row['Balls']}    
    | wickets2 = {wkt}
    | bowl avg2 = {BowlAvg}
    | fivefor2 = {w5}
    | tenfor2 = -
    | best bowling2 = 
    | catches/stumpings2 = {st}/{ct}
    '''

    infoEND = f'''
    | source = {cricinfoREF} کرک انفو
{infoClosing}
'''
    if T20 == 'Y':
        # T20 Info
        infoBox = info1 + infoT20 + infoODI + infoT20TestDet + infoODIDet + infoEND
    else:
        # Test Info
        infoBox = info1 + infoTest + infoODI + infoT20TestDet + infoODIDet + infoEND

    return infoBox


def addRef(row):
    p = '|'
    startRef = '<ref>{{cite web'
    endRef = '}} </ref>'

    urladdr1 = "https://www.espncricinfo.com/england/content/player/" + \
        row['RefAddr1']
    web1 = "cricinfo"
    web3 = "sportskeeda"
    curDate = "27 مارچ 2021"

    reftitle1 = p + 'title=' + str(row['Title'])
    url1 = p + 'URL=' + urladdr1
    web1 = p + 'website=' + web1
    date = p + 'date=' + curDate
    REF1 = startRef + reftitle1 + url1 + web1 + date + endRef

    #reftitle2 = p + 'title=' + str(row['RefTitle2'])
    #url2 = p + 'URL=' + str(row['RefAddr2'])
    web2 = p + 'website=' + web1
    date = p + 'date=' + curDate
    #REF2 = startRef + reftitle2 + url2 + web2 + date + endRef
    REF2 = '''<ref>{{cite web 
    |url=https://stats.espncricinfo.com/ci/engine/records/index.html?class=8;id=1026;type=team
    |title=انگلش خواتین کرکٹ کھلاڑی
    |website=کرک انفو
    |date=25 مارچ 2021
    }}</ref>
    '''

    REF3 = f'''
    <ref>{{cite web 
    |url=https://www.sportskeeda.com/team/indian-women-cricket
    |title=Indian Women's Cricket Team
    |website={web3}
    |date=25 مارچ 2021 
    }}</ref>
    '''

    return (REF1, REF2, REF3)


def categorize():
    cat_women_india = f'''
[[زمرہ:بقید حیات شخصیات]]
[[زمرہ:بیسویں صدی کی آسٹریلوی خواتین]]
[[زمرہ:آسٹریلیا کی خواتین ایک روزہ کرکٹ کھلاڑی]]
    '''
    return cat_women_india


def urWikiPage(title, wikitxt):
    site = pywikibot.Site('ur', 'wikipedia')

    urPage = Page(site, title)
    urPage.text = wikitxt

    tag = "(ٹیگ: ترمیم ماخذ 2021ء)"
    page_summary = title + " پر نیا صفحہ" + tag

    # Save page to Urdu Wikipedia
    urPage.save(summary=page_summary, minor=False)


def intro(title, bd, city, cntry, BAT, BOWL, mat, tmat, T20, ref1):
    bTitle = btag + title + btag
    cntry = s + cntry
    line1 = bTitle + cntry + s + f"کی خاتون کرکٹ کھلاڑی ہیں" + ref1 + "۔ "
    line2 = title + s + city + '،' + cntry + " میں " + bd + "  کو پیدا ہوئیں۔"

    if T20 == 'Y':
        line3 = " انھوں نے ٹی ٹوئنٹی اور ون ڈے کرکٹ کھیلی ہے۔"
        t_t20 = " ٹی ٹوئنٹی "
    else:
        line3 = " انھوں نے ٹیسٹ کرکٹ اور ون ڈے کرکٹ کھیلی ہے۔"
        t_t20 = " ٹیسٹ "

    line4 = "وہ" + s + BAT + " کرتی ہیں اور  " + BOWL + " گیند باز ہیں۔ "
    line5 = line1 + line2 + line3 + line4

    lines = line5
    aur = " اور "
    TotCric = f' انھوں نے بین الاقوامی سطح پر مجموعی طور پر'
    TotCric += str(tmat) + t_t20 + aur + str(mat) + \
        s + "ون ڈے میچ کھیلے۔" + nl
    all_lines = lines + TotCric
    return all_lines


def addODIcareer(title, ODEB, fmat, avg, score, HS, fifty, c, balls, wkt, bavg, w5, cat):
    odi = "=== ون ڈے کیریئر ===" + nl
    odi += title + " نے پہلا بین الاقوامی ون ڈے میچ " + \
        ODEB + " کے خلاف سن " + fmat + " میں کھیلا۔ " + nl
    odi += "انھوں نے " + avg + " کی اوسط سے کل " + score + \
        " رنز بنائے جس میں سب سے زیادہ " + HS + s + "کا اسکور بھی شامل ہے۔ "
    c_fif = odi + " وہ" + fifty + " نصف سنچری کرنے میں کامیاب رہیں۔ "
    odi = c_fif + "انھوں نے کل " + balls + \
        " گیندیں پھینکیں اور " + wkt + s + "وکٹیں حاصل کیں۔"
    odi += " ان کی باؤلنگ کی اوسط" + bavg + \
        "رہی جس میں " + w5 + " پانچ وکٹیں بھی شامل ہیں۔"
    odi += title + s + cat + " کیچ پکڑنے میں کامیاب رہیں۔" + nl
    line6 = "انھوں نے چھوٹی عمر میں مقامی کرکٹ کا آغاز کر دیا تھا، اس کے بعد وہ مختلف کلبوں کی طرف سے کھیلتی رہیں اور فرسٹ کلاس کرکٹ بھی کھیلی۔"
    odi += nl + line6 + nl

    return odi


def addTESTcareer(title, TDEB, tf, avg, trun, ths, T50, T100, balls, wkt, bavg, w5, tcat):
    tst = nl + "=== ٹیسٹ کیریئر ===" + nl
    tst += title + " نے پہلا بین الاقوامی ٹیسٹ میچ " + \
        TDEB + " کے خلاف سن " + tf + " میں کھیلا۔ " + nl
    tst += "انھوں نے کل " + trun + " رنز بنائے جس میں سب سے زیادہ "
    tst += ths + " کا اسکور بھی شامل ہے۔" + nl
    #tst += " وہ" + T50 + " " + " پچاس کرنے میں کامیاب رہیں۔"
    #odi += title + s + cat + " کیچ پکڑنے میں کامیاب رہیں۔"
    return tst


def addT20career(title, TDEB, tf, avg, trun, ths, T50, T100, balls, wkt, bavg, w5, tcat):
    t20 = nl + "=== ٹی ٹونٹی کیریئر ===" + nl
    t20 += title + " نے پہلا بین الاقوامی T20 میچ " + \
        TDEB + " کے خلاف سن " + tf + " میں کھیلا۔ " + nl
    t20 += "انھوں نے کل " + trun + " رنز بنائے جس میں سب سے زیادہ "
    t20 += ths + " کا اسکور بھی شامل ہے۔" + nl

    return t20


def createArticle(row):
    #global wikitext
    title = row['Title']
    bTitle = btag + title + btag
    fmat = str(row['First'])
    lmat = str(row['Last'])
    mat = str(row['Mat'])
    score = str(row['Runs'])
    HS = str(row['HS'])
    avg = str(row['Avg'])
    cent = str(row['CENT'])
    fifty = str(row['Fifty'])
    avg = str(row['Avg'])
    balls = str(row['Balls'])
    wkt = str(row['WKT'])
    bbowl = "-"  # str(row['BBM'])
    bavg = str(row['BAvg'])
    w5 = str(row['WI5'])
    ct = str(row['Cat'])
    st = str(row['ST'])
    batS = str(row['BAT'])
    bowlS = str(row['BOWL'])
    bd = str(row['Bday'])
    city = str(row['City'])
    ODEB = str(row['ODEB'])
    cntry = str(row['CNTRY'])

    t20 = row['T20']
    # TEST Info
    tdeb_yr = str(row['TFirst'])
    tdeb = str(row['TDEB'])
    tmat = str(row['TMat'])
    twkt = str(row['TWKT'])
    truns = str(row['TRUN'])
    ths = str(row['THS'])
    tct = str(row['TCT'])
    t50 = str(row['T50'])
    t100 = str(row['T100'])

    t20 = row['T20']

    refs = addRef(row)
    info = infoBox(title, row, t20)

    outfile = os.path.join(DIR, title + '.txt')
    with open(outfile, 'w', encoding='utf-8') as ofile:

        ofile.write(f'{info}')
        wikitext = nl + info

        introLN = intro(title, bd, city, cntry, batS,
                        bowlS, mat, tmat, t20, refs[0])
        ofile.write(f'\n{introLN}')
        wikitext += introLN + nl

        cric_car = nl + "== کرکٹ کیریئر ==" + nl
        ofile.write(f'{cric_car}')
        wikitext += cric_car + nl

        odi_car = addODIcareer(title, ODEB, fmat, avg,
                               score, HS, fifty, cent, balls, wkt, bavg, w5, ct)
        ofile.write(f'{odi_car}')
        wikitext += odi_car + nl

        if t20 == 'Y':
            t20_car = addT20career(
                title, tdeb, tdeb_yr, avg, truns, ths, t50, t100, balls, wkt, bavg, w5, tct)
            ofile.write(f'{t20_car}')
            wikitext += t20_car + nl
        else:
            test_car = addTESTcareer(
                title, tdeb, tdeb_yr, avg, truns, ths, t50, t100, balls, wkt, bavg, w5, tct)
            ofile.write(f'{test_car}')
            wikitext += test_car + nl

        ofile.write(f'\n\n{ref}')
        wikitext += ref

        cats = categorize()
        ofile.write(f'\n{cats}')
        wikitext += cats

        # print(wikitext)
        return title, wikitext


data = pd.read_excel(excelFile, 'CUR')
df = pd.DataFrame(data, columns=['Title', 'First', 'Last', 'Mat', 'Runs', 'HS', 'Avg', 'Fifty', 'CENT', 'Balls', 'WKT', 'WI5',
                                 'BAvg', 'Cat', 'ST', 'BAT', 'BOWL', 'Bday', 'City', 'CNTRY', 'ODEB', 'T20', 'TDEB', 'TFirst',
                                 'TMat', 'TRUN', 'THS', 'TAV', 'T100', 'T50', 'TBall', 'TWKT', 'TBAv', 'TCT', 'Role', 'RefAddr1'])

lst_article = []
df = df.fillna(NA)
for idx, datarow in df.iterrows():
    wikiTitle, article = createArticle(datarow)
    lst_article.append((wikiTitle, article))

wikiSave = True

# Save WikiPage for each article
if wikiSave is True:
    for article in lst_article:
        wikiTitle = article[0]
        urText = article[1]
        print(wikiTitle)
        urWikiPage(wikiTitle, urText)
        print(f'Wiki Page {wikiTitle} is created and saved')
        time.sleep(10)

# if __name__ == "__main__":
#     main()
