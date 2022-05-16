import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE = Path('C:\LEARNING\MISC\WebScraping')

# Link of AlFarooq Typing by Shamshaad
MEHFIL_URL = 'https://tinyurl.com/alfarooq-urduweb'
html = requests.get(MEHFIL_URL).text
soup = BeautifulSoup(html, "lxml")

#articles = soup.findAll("div")
#items = dict()

#Previously it was "messageText" class within blockquote tag, now it is within div tag
article_rows = soup.find_all("div", class_="bbWrapper")

try:

    if article_rows:
        # if want to print all article_rows then remove indexing of first element article_rows[0]
        articleSoup = BeautifulSoup(str(article_rows[0]), "lxml")
        articleText = articleSoup.get_text()

        # regex pattern for matching square brackets and text within it [*]
        strCleaned = re.sub("[\[].*?[\]]", "",  articleText)

        ofile = BASE / 'AlFarooq.txt'
        with open(ofile, 'w', encoding='utf-8') as f:
            f.write(strCleaned)
    else:
        print(article_rows)
        
except Exception as e:
    print(e)