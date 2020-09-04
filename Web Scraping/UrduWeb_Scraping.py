import re
import requests
from bs4 import BeautifulSoup

# Link of Urdu Novel Posts
MEHFIL_URL = 'https://www.urduweb.org/mehfil/threads/%D9%88%DB%81-%D8%AC%D9%88-%D9%82%D8%B1%D8%B6-%D8%B1%DA%A9%DA%BE%D8%AA%DB%92-%D8%AA%DA%BE%DB%92-%D8%AC%D8%A7%D9%86-%D9%BE%D8%B1-%D8%A7%D8%B2-%D9%81%D8%B1%D8%AD%D8%AA-%D8%A7%D8%B4%D8%AA%DB%8C%D8%A7%D9%82-%D9%85%DA%A9%D9%85%D9%84-%D9%86%D8%A7%D9%88%D9%84.6032/'
html = requests.get(MEHFIL_URL).text
soup = BeautifulSoup(html, "lxml")

#articles = soup.findAll("div")

items = dict()
article_rows = soup.findAll("blockquote", {"class": "messageText"})

# if want to print all article_rows then remove indexing of first element article_rows[0]
articleSoup = BeautifulSoup(str(article_rows[0]), "lxml")
articleText = articleSoup.get_text()

# regex pattern for matching square brackets and text within it [*]
strCleanred = re.sub("[\[].*?[\]]", "",  articleText)

#print(strCleaned)

ofile = r'QarzHaiJaanPar.txt'
with open(ofile, 'w', encoding='utf-8') as f:
    f.write(str1)
