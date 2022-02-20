import time
import os
#from pathlib import Path
import pandas as pd
from pywikibot.page import Page
import pywikibot
import argparse

DIR = r'<PLACEHOLDER>'
excelFile = os.path.join(DIR, 'WomenPolitician.xlsx')


nl = '\n'
s = " "
spc = " "
wikitext = ""
ref = '== حوالہ جات ==' + nl + '{{حوالہ جات}}'
title = ""
NA = 'غیرموجود'


def infoBox(title, prov, pparty, icity):
    provAss2 = "[[صوبائی اسمبلی پاکستان]] کی رکن "
    city = icity
    residence = f"صوبہ {prov} "
    infoStart = "{{ Infobox officeholder"
    infoEnd = "}}"
    infoBox = f'''
    {infoStart}
      | name = {title}
      | honorific - suffix =
      | office = {prov} {provAss2}
      | term_start = 2018 اگست 13 
      | term_end = 2023 13 اگست
      | constituency1 = خواتین کے لئے مخصوص نشست
      | nationality = پاکستانی
      | religion =اسلام 
      | residence  = {city} {residence}
      | occupation  = سیاستدان
      | profession  = 
      | party = [[{pparty}]]
    {infoEnd}
    '''
    return infoBox


def addRef(row,prov):
    p = '|'
    startRef = '<ref>{{cite web'
    endRef = '}} </ref>'
    web1 = prov + " صوبائی اسمبلی سرکاری ویب"
    web2 = "پاک ووٹر"
    web3 = "FAFEN"
    curDate = "25 مارچ 2021"

    reftitle1 = p + 'title=' + str(row['RefTitle1'])
    url1 = p + 'URL=' + str(row['RefAddr1'])
    web1 = p + 'website=' + web1
    date = p + 'date=' + curDate
    REF1 = startRef + reftitle1 + url1 + web1 + date + endRef

    reftitle2 = p + 'title=' + str(row['RefTitle2'])
    url2 = p + 'URL=' + str(row['RefAddr2'])
    web2 = p + 'website=' + web2
    date = p + 'date=' + curDate
    REF2 = startRef + reftitle2 + url2 + web2 + date + endRef

    reftitle3 = p + 'title=' + str(row['RefTitle3'])
    url3 = p + 'URL=' + str(row['RefAddr3'])
    web3 = p + 'website=' + web3
    date = p + 'date=' + curDate
    REF3 = startRef + reftitle3 + url3 + web3 + date + endRef

    return (REF1, REF2, REF3)


def politicalContent(pLine, title, pparty, prov, eYR):
    if eYR == NA:
        pLine1 = pLine
    else:
        pLine1 = pLine + title + spc + \
            str(eYR) + " کے عام انتخابات میں خواتین کے لیے مخصوص نشست پر "
        pLine1 += pparty + " کی امیدوار کے طور پر " + \
            prov + " کی صوبائی اسمبلی کے لئے منتخب ہو گئیں۔ " + nl

    return pLine1


def addCMT(cmt1, cmt2, cmt3):
    cmtln = []
    if cmt1 == NA:
        cmtln.append(NA)
    else:
        cmtln.append(cmt1)

    if cmt2 == NA:
        cmtln.append(NA)
    else:
        cmtln.append(cmt2)

    return cmtln


def addBills(bill1, bill2, bill3):
    bills = []
    bills.append(bill1)
    bills.append(bill2)
    bills.append(bill3)

    return bills


def resolution(resLine, title, res1, res2):
    if res1 == NA:
        resln = resLine
    else:
        resH = nl + "=== صوبائی اسمبلی قرارداد ===" + nl

        resln = resH + title + " نے " + res1 + "  قرارداد پیش کی۔"
        resln += nl + res2 + " کی قرارداد پیش کی۔"

    return resln


def categorize(nl, prov, party):
    if prov == 'پنجاب':
        if party == 'مسلم لیگ (ن)':
            cat_pnb_pmln = f'''
            {nl}[[زمرہ:پنجاب کے سیاست دان]]
            {nl}[[زمرہ:مسلم لیگ (ن) کے ارکان صوبائی اسمبلی (پنجاب)]]
            {nl}[[زمرہ:بقید حیات شخصیات]]            
            {nl}[[زمرہ:مسلم لیگ (ن) کی مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_pnb_pmln
        elif party == 'پاکستان تحریک انصاف':
            cat_pnb_pti = f'''
            {nl}[[زمرہ:پنجاب کے سیاست دان]]
            {nl}[[زمرہ:پاکستان تحریک انصاف کے ارکان صوبائی اسمبلی (پنجاب)]]
            {nl}[[زمرہ:بقید حیات شخصیات]]            
            {nl}[[زمرہ:پاکستان تحریک انصاف کی مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_pnb_pti
        else:
            cat_pnb_misc = f'''
            {nl}[[زمرہ:پنجاب کے سیاست دان]]
            {nl}[[زمرہ:بقید حیات شخصیات]]            
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_pnb_misc

    elif prov == 'سندھ':
        if party == 'متحدہ قومی موومنٹ':
            cat_snd_mqm = f'''
            {nl}[[زمرہ:سندھ کے سیاست دان]]            
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_snd_mqm
        elif party == 'پاکستان تحریک انصاف':
            cat_snd_pti = f'''
            {nl}[[زمرہ:سندھ کے سیاست دان]]            
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_snd_pti
        else:
            cat_snd_misc = f'''
            {nl}[[زمرہ:سندھ کے سیاست دان]]            
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_snd_misc
    elif prov == 'خیبر پختونخوا':
        if party == 'پاکستان تحریک انصاف':
            cat_kpk_pti = f'''
            {nl}[[زمرہ:خیبر پختونخوا کے سیاست دان]]
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_kpk_pti
        elif party == 'عوامی نیشنل پارٹی':
            cat_kpk_anp = f'''
            {nl}[[زمرہ:خیبر پختونخوا کے سیاست دان]]
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_kpk_anp
        else:
            cat_kpk_misc = f'''
            {nl}[[زمرہ:خیبر پختونخوا کے سیاست دان]]
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_kpk_misc

    elif prov == 'بلوچستان':
        if party == 'پاکستان تحریک انصاف':
            cat_blch_pti = f'''
            {nl}[[زمرہ:بلوچستان کے سیاست دان]]
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_blch_pti
        else:
            cat_blch_misc = f'''
            {nl}[[زمرہ:بلوچستان کے سیاست دان]]
            {nl}[[زمرہ:بقید حیات شخصیات]]
            {nl}[[زمرہ:مخصوص نشستوں پر خواتین سیاستدان]]
            '''
            return cat_blch_misc


# def write_output(text):
#     outfile = os.path.join(DIR, )
#     with open(outfile, 'w', encoding='utf-8') as ofile:
#         ofile.write(text)


def urWikiPage(title, wikitxt):
    site = pywikibot.Site('ur', 'wikipedia')

    urPage = Page(site, title)
    urPage.text = wikitxt

    tag = "(ٹیگ: ترمیم ماخذ 2021ء)"
    page_summary = title + " پر نیا صفحہ" + tag

    # Save page to Urdu Wikipedia
    urPage.save(summary=page_summary, minor=False)


def createArticle(row):
    global wikitext
    btag = "'''"
    start = "{{-start-}}"
    stop = "{{-stop-}}"
    title = row['Title']
    bTitle = btag + title + btag
    pparty = row['Party']
    city = row['City']
    prov = row['Province']
    bill = row['Bill']
    cmt1 = row['B_C1']
    cmt2 = row['B_C2']
    cmt3 = row['B_C3']
    eYR3 = row['EYR3']
    oath = row['DateOath']
    YR = str(row['EdYR'])
    B_M = row['B_M']
    Major = row['Major']
    spouse = row['Husband']
    res1 = row['Res1']
    res2 = row['Res2']
    cn1 = row['CAN1']
    cn2 = row['CAN2']
    cn3 = row['CAN3']

    refs = addRef(row,prov)
    info = infoBox(title, prov, pparty, city)

    outfile = os.path.join(DIR, title + '.txt')
    with open(outfile, 'w', encoding='utf-8') as ofile:
        # ofile.write(f'{start}\n')

        ofile.write(f'{info}')
        wikitext += info

        # ofile.write(f'\n{title}')
        line1 = f" ایک پاکستانی سیاستدان ہیں، جن کی سیاسی وابستگی "
        #refs = addRef(row)
        line1 = title + line1 + pparty + \
            " سے ہے۔" + str(refs[0]) + str(refs[1])

        ofile.write(f'\n{line1}')
        wikitext += nl + line1

        edu = f"{title} نے {Major}" + " کے مضمون میں سال " + \
            YR + " میں " + B_M + " کی ڈگری حاصل کی تھی۔ "
        ofile.write(f'\n{edu}')
        wikitext += edu

        line2 = title + " سن " + str(eYR3) + " سے "
        line2 += prov + " کی صوبائی اسمبلی  کی رکن رہی ہیں۔ "
        ofile.write(f'\n{line2}')
        wikitext += line2

        if spouse != NA:
            wedding = title +s+ "شادی شدہ ہیں اور ان کے شوہر کا نام" +s+ spouse +s+ "ہے۔"
            ofile.write(f'\n{wedding}')
            wikitext += wedding + nl

        oathLine = title + " نے " + oath + " کو " + prov
        oathLine += " صوبائی اسمبلی کی رکنیت کا حلف اٹھایا۔ "
        ofile.write(f'\n{oathLine}')
        wikitext += oathLine

        politicHead = nl + "== سیاسی کیریئر ==" + nl
        ofile.write(f'\n{politicHead}')
        wikitext += politicHead + nl

        pLine = ""
        # pLine1 = politicalContent(pLine, title, pparty, prov, eYR1)
        # pLine2 = politicalContent(pLine1, title, pparty, prov, eYR2)
        pLine3 = politicalContent(pLine, title, pparty, prov, eYR3)
        ofile.write(f'\n{pLine3}')
        wikitext += pLine3 + nl

        Performance = title + spc + \
            " متحرک اور سرگرم عمل صوبائی اسمبلی رکن ہیں جو قائمہ کمیٹیوں ،"
        Performance += " توجہ دلاؤ نوٹس اور اسمبلی کی قراردادوں میں شریک رہیں۔ "
        ofile.write(f'\n{Performance}')
        wikitext += nl + Performance + nl

        resLine = ""
        if res1 == NA:
            pass
        else:
            resln = resolution(resLine, title, res1, res2)
            #ref3 = str(refs[1])
            ofile.write(f'\n{resln}{refs[2]}')
            wikitext += nl + resln + refs[2] + nl

        if bill == 'Y':
            billHead = nl + "=== ترامیمی بل ==="
            billLn = "وہ صوبائی اسمبلی میں کئی ترامیمی بل پیش کر چکی ہیں، جن میں سے چند مندرجہ ذیل ہیں: "
            ofile.write(f'\n{billHead}')
            ofile.write(f'\n{billLn}')
            wikitext += nl + billLn
            wikitext += nl + billHead + nl

            bills = addBills(cmt1, cmt2, cmt3)
            ofile.write(f'\n{bills[0]}')
            ofile.write(f'\n{bills[1]}')
            ofile.write(f'\n{bills[2]}')
            wikitext += bills[0] + nl + bills[1] + nl + bills[2] + nl

        elif bill == NA:
            standComm = nl + "=== صوبائی کمیٹیوں کی رکنیت ===" + nl
            commLn = "مندرجہ ذیل کمیٹیوں کی رکن رہی ہیں:"
            ofile.write(f'\n{standComm}')
            ofile.write(f'\n{commLn}')
            wikitext += nl + commLn
            wikitext += nl + standComm + nl

            cmts = addCMT(cmt1, cmt2, cmt3)
            if cmts[0] != NA:
                ofile.write(f'\n{cmts[0]}')
                ofile.write(f'\n{cmts[1]}')
                ofile.write(f'\n{cmts[2]}')
                wikitext += cmts[0] + nl + cmts[1] + nl + cmts[2] + nl

        if cn1 == NA:
            pass
        else:
            canHead = nl + "=== توجہ دلاؤ نوٹس ===" + nl
            canLn = "وہ صوبائی اسمبلی میں کئی معاملات پر توجہ دلاؤ نوٹس بھی پیش کرتی رہی ہیں، جن میں سے چند مندرجہ ذیل ہیں: "
            ofile.write(f'\n{canHead}')
            ofile.write(f'{canLn}')
            ofile.write(f'\n{cn1}\n{cn2}\n{cn3}')
            wikitext += canHead + canLn + nl
            wikitext += cn1 + nl + cn2 + nl + cn3 + nl

        ofile.write(f'\n\n{ref}')
        wikitext += ref

        cats = categorize(nl, prov, pparty)
        ofile.write(f'\n{cats}')
        wikitext += cats

        return title, wikitext

        # ofile.write(f'\n{stop}\n')

        #line2 = f"{row['Title']} سن {row['ElectYr']} سے سیاسی جماعت {row['Party']} سے جڑی {row['Province']} کی صوبائی اسمبلی کی رکن رہی ہیں۔"
        #text = bTitle + nl + line1 + nl + line2 + nl + nl
        #finalText = start + text + stop
        # write_output(finalText)


data = pd.read_excel(excelFile, 'CUR')
df = pd.DataFrame(
    data, columns=['Num', 'Title', 'DateOath', 'Party', 'DateBirth', 'EYR3', 'EdYR', 'B_M', 'Major', 'Husband', 'Status', 'City', 'Province', 'Bill',
                   'B_C1', 'B_C2', 'B_C3', 'CAN1', 'CAN2', 'CAN3', 'Res1', 'Res2', 'RefTitle1', 'RefTitle2', 'RefTitle3', 'RefAddr1', 'RefAddr2', 'RefAddr3'])

lst_article = []
df = df.fillna(NA)
for idx, datarow in df.iterrows():
    wikiTitle, article = createArticle(datarow)
    lst_article.append((wikiTitle, article))

wikiSave = False

# Save WikiPage for each article
if wikiSave is True:
    for article in lst_article:
        wikiTitle = article[0]
        urText = article[1]
        print(wikiTitle)
        urWikiPage(wikiTitle, urText)
        print(f'Wiki Page {wikiTitle} is created and saved')
        time.sleep(12)

# if __name__ == "__main__":
#     main()
