import encodings
from venv import create
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import csv
from csv import DictReader

BASE = Path('D:\Wikipedia\code_output\FNF2022')

nl = '\n'
s = " "
c = ' ،'
ds = "۔ "
btag = "'''"
NA = 'غیرموجود'
ls = "* "
title = ''
d = {}


def enURTransliterate():
    csvfile = BASE / 'EN_UR_CRIC.csv'

    with open(csvfile, encoding='utf-8') as cfile:
        csv_reader = csv.reader(cfile)
        for row in csv_reader:
            d[row[0]] = row[1]

    return d


def inFileReader():
    csvfile = BASE / 'women_cric_title.csv'
    dictInfile = {}
    with open(csvfile, encoding='utf-8') as cfile:
        dcsv_reader = DictReader(cfile, delimiter='|')

        # get column names ENG:URDU:CricLink1
        col = dcsv_reader.fieldnames

        for row in dcsv_reader:
            dictInfile[col[0]] = row['ENG']
            dictInfile[col[1]] = row['URDU']
            dictInfile[col[2]] = row['CricLink1']

    return dictInfile


def addRef(REFURL):
    p = '|'
    startRef = '<ref>{{cite web'
    endRef = '}} </ref>'

    web1 = "cricinfo"
    curDate = "01 مارچ 2022"

    refTitle1 = p + 'title=' + urTitle
    url1 = p + 'URL=' + REFURL
    web1 = p + 'website=' + web1
    date = p + 'date=' + curDate
    REF1 = startRef + refTitle1 + url1 + web1 + date + endRef

    return REF1


def playerPersonal(playerGrid):
    playerDemo = {}
    for div in playerGrid:
        title = div.find("p")
        Value = div.find("h5")
        print(title.text, Value.text)
        playerDemo[title.text] = Value.text

    return playerDemo


def playerTeams(Teams):
    playerTeams = []
    for heading in Teams.find_all('h5'):
        title = heading.text
        #Value = div.find("h5")
        #print(title.text, Value.text)
        playerTeams.append(title)

    return playerTeams


def table_header(tbl):
    theader = tbl.findAll('thead')
    header_titles = theader[0].text
    t_header = [title for title in header_titles.split('\n') if title != ""]
    t_header[0] = 'Num'
    t_header[1] = 'Country'
    t_header.append('Extra21')

    print(t_header)

    return t_header


def tableDataText(tbl_stats):
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'):  # td (data) or th (header)
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]

    rows = []
    trs = tbl_stats.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow:  # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs:  # for every table row
        rows.append(rowgetDataText(tr, 'td'))  # data row
    return rows


def df_table(tbl, i):
    tblrows = tableDataText(tbl)

    dftable = pd.DataFrame(tblrows[1:], columns=tblrows[0])

    # Using DataFrame.insert() to add a column
    if i == 0:
        dftable["CAT"] = "Batting"
    elif i == 1:
        dftable["CAT"] = "Bowling"
    elif i == 2:
        dftable["CAT"] = "Records"

    dftable.head(4)

    return dftable


def intro(title, playerInfoDict,  ref1):
    bTitle = btag + title + btag
    Born = playerInfoDict['Born']
    #bday, year, city, prov, cntry = Born.split(',')

    line1 = bTitle + s + Born + s + d['ki'] + s + \
        d['khatoon'] + s + d['cric'] + s + \
        d['khiladi'] + s + d['hein'] + s + nl + addRef(ref1) + ds + nl

    line2 = title + s + Born + s + \
        d['mein'] + s + Born + s + d['ko'] + \
        s + d['paida'] + s + d['hoeen'] + s+ds

    line3 = d['unho'] + s + d['nay']+s+d['test']+s + \
        d['cric']+s+d['aur']+s+d['odi']+s + \
        d['cric']+s+d['khaili']+s+d['hai'] + ds
    t_t20 = " ٹیسٹ "

    line4 = d['wo'] + s + d['rhb'] + s + d['bat'] + \
        s + d['karti'] + s + d['hein'] + s + d['aur'] + s + \
        d['offbreak'] + s + d['bowler'] + s + d['hein'] + s
    line5 = line1 + line2 + line3 + line4

    lines = line5

    #TotCric = f' انھوں نے بین الاقوامی سطح پر مجموعی طور پر'
    TotCric = d['unho']+s+d['nay']+s+d['international']+s+d['sata']+s+d['par']+s+d['majmoi']+s + \
        d['taur']+s+d['par']+s+d['achi']+s + \
        d['cric']+s+d['khaili']+s+d['hai']+s+ds

    all_lines = lines + TotCric
    return all_lines

# Teams player is associated with


def Teams(lstPlayerTeams):
    TeamLines = nl + "== ٹیمیں ==" + nl
    TeamLines += urTitle + s + d['nay']+s + d['apnay']+s + d['career']+s + d['mein'] + s + d['kayi']+s + d['teamo']+s + d['ki']+s + \
        d['numaindagi'] + s + d['ki']+s + d['jin']+s + d['mein']+s + d['qabil']+s + d['zikr']+s + \
        d['mundarjazail'] + s + d['hein'] + ":" + nl

    for team in lstPlayerTeams:
        TeamLines += ls + team + nl

    return TeamLines


def addBatting(df, cric_format):
    if cric_format == 'ODI':
        cricform = d['odi']
        batField = nl + "===" + cricform + s + d['career'] + "===" + s + nl
    elif cric_format == 'T20':
        cricform = d['T20']
        batField = nl + "===" + cricform + s + d['career'] + "===" + s + nl
    elif cric_format == 'TEST':
        cricform = d['test']
        batField = nl + "===" + cricform + s + d['career'] + "===" + s + nl

    batField += urTitle + s + d['nay']+s + df['Mat'] + \
        s + cricform + s + d['mat']+s + d['khailay']+c+s

    InnsLn = d['jis']+s+d['mein']+s + \
        df['Inns'] + s + d['shamil']+s+d['hein']+c+s

    notoutLn = d['wo']+s+df['NO'] + s + \
        d['baar']+s+d['notout']+s+d['rahein']+ds

    RunsLn = urTitle + s + d['nay']+s + \
        df['Runs'] + s + d['score']+s+d['kiye']+ds

    AVG = d['unho']+s + d['nay']+s + df['Ave']+s + d['ki'] + \
        s + d['avg']+s + d['se']+s+d['score']+s+d['banaye']+c+s

    HS = d['un'] + s + d['ka'] + s+d['behtreen'] + \
        s+d['score']+s + df['HS']+s + d['raha']+ds

    batField += InnsLn + notoutLn + RunsLn + AVG + HS

    cent = s + d['centuriyan'] + s
    cent_50 = d['unho'] + s + d['ne'] + s + df['50s'] + s + d['nisf'] + \
        cent + s + d['aur'] + s + df['100s'] + cent + d['banayi']

    four = d['unho'] + s + d['ne'] + s+d['apnay']+s + \
        d['career']+s+d['mein']+s + df['6s'] + s+d['chakay']+s

    six = d['aur']+s + df['4s'] + s+d['chaukay']+s+d['maaray']+ds

    catch = d['unho'] + s + d['ne'] + s+d['apnay']+s+d['career'] + \
        s+d['mein']+s + df['Ct'] + s + d['catch']+s + d['pakray'] + ds + nl

    batField += cent_50 + four + six + catch

    return batField


def addBatTestODIT20(df_batField):
    df_bat_test = df_batField.iloc[0]
    test = addBatting(df_bat_test, 'TEST')

    df_bat_ODI = df_batField.iloc[1]
    odi = addBatting(df_bat_ODI, 'ODI')

    df_bat_T20 = df_batField.iloc[2]
    t20 = addBatting(df_bat_T20, 'T20')

    battingLines = test + odi + t20

    ExtraLn = "انھوں نے چھوٹی عمر میں مقامی کرکٹ کا آغاز کر دیا تھا، اس کے بعد وہ مختلف کلبوں کی طرف سے کھیلتی رہیں اور فرسٹ کلاس کرکٹ بھی کھیلی۔"

    return battingLines


# Getting english and Urdu title along with Reference Link extracted from csv file
titleDict = inFileReader()
engTitle = titleDict.get('ENG') + '.txt'
urTitle = titleDict.get('URDU')
refLink1 = titleDict.get('CricLink1')

#WOMEN_CRIC_URL1 = 'https://www.espncricinfo.com/player/nicole-bolton-267611'
WOMEN_CRIC_URL = refLink1
page = requests.get(WOMEN_CRIC_URL)
soup = BeautifulSoup(page.content, 'html.parser')

#playercard = soup.find_all("div", class_="player-card-padding")

# Player Overview Grid containing personal info in a DIV
playerGrid = soup.find("div", class_="player_overview-grid")
playerInfoDict = playerPersonal(playerGrid)

# Player Teams info in a DIV grid class
playerTeamSoupObj = soup.find("div", class_="overview-teams-grid mb-4")
lstPlayerTeams = playerTeams(playerTeamSoupObj)

# Extract Table for Batting & Bowling
tbl_stats = soup.select(".table")

# Creating dictionary of Dataframes for Batting, bowling and records
df_dict_comp = {i: df_table(tbl, i) for i, tbl in enumerate(tbl_stats)}

en_ur_dict = enURTransliterate()
df_bat = df_dict_comp[0]


outfile = BASE / engTitle
with open(outfile, 'w', encoding='utf-8') as ofile:

    # Intro of Urdu Article
    introLN = intro(urTitle, playerInfoDict, refLink1)
    ofile.write(f'\n{introLN}')
    wikitext = introLN + nl

    # Add Teams of player
    teamPL = Teams(lstPlayerTeams)
    ofile.write(f'\n{teamPL}')
    wikitext = teamPL + nl

    # Add Batting text for Test, ODI and T20
    batting_text = addBatTestODIT20(df_bat)
    ofile.write(f'\n{batting_text}')
    wikitext = batting_text + nl

    # Add Reference Template
    hawalajaat = d['hawalajaat']
    ref_template = f'== {hawalajaat} ==' + nl + '{{' + hawalajaat + '}}'
    ofile.write(f'\n\n{ref_template}')
    wikitext += ref_template
