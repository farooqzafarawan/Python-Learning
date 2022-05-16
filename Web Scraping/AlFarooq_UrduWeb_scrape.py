# Scraping a book typing thread in UrduMehfil forum
# In[25]: 
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv 
import time

BASE = Path('C:\LEARNING\MISC\WebScraping')

# In[27]:
def getSoupObject(MEHFIL_URL):
    html = requests.get(MEHFIL_URL).content
    soup = BeautifulSoup(html, "lxml")
    return soup


# In[28]:
def scrapePosts(soup):
    articles = soup.select('article > div.bbWrapper')
    lst_articles = [post for post in articles]
    return lst_articles

# In[31]:
def textClean(text):
    html_tags = re.compile('<.*?>')
    cleanText = re.sub(html_tags, '', str(text))
    return cleanText

# %%
# File for writing new records
def writeFile(lst_articles, textClean, csvwritef):
    with open(csvwritef, mode='w', newline='', encoding='utf8') as writef:
    #writer = csv.writer(csvwrite, quoting=csv.QUOTE_MINIMAL)
        for i,text in enumerate(lst_articles):
            #print(f'Printing Item {i}')
            textPara = textClean(text)
            writef.write(textPara)

# %%
def multiPageScraping(BASE, URL, num):

    for i in range(1,num):
        csvFile = 'alFarooq' + '-' + str(i) + '.txt'
        csvwritef =  BASE / csvFile

        if i == 1:
            soup = getSoupObject(URL)
        else:
            URL_PG = URL + '/' + 'page-' + str(i)
            soup = getSoupObject(URL_PG)

        if i == 3:
            print(URL_PG)

        lst_articles = scrapePosts(soup)

        writeFile(lst_articles, textClean, csvwritef)
        print(f'Complete Page {i}')
        time.sleep(1)

# %%
# Scrape continous pages of same thread

# Link of AlFarooq Typing by Shamshaad
MEHFIL_URL = 'https://tinyurl.com/alfarooq-urduweb'

multiPageScraping(BASE, MEHFIL_URL, 21)

