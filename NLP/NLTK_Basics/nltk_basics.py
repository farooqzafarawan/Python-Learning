# pip install nltk
import nltk
#from nltk.book import *

'''NLTK includes a small selection of texts from the Project Gutenberg electronic text
archive, which contains some 25,000 free electronic books, hosted at http://www.gutenberg.org/.''' 
nltk.download('gutenberg')

from nltk.corpus import gutenberg
gutenberg.fileids()

'''program displays three statistics for each text: average word length, average sentence length, 
and the number of times each vocabulary item appears in the text on
average (our lexical diversity score). '''
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    
    print (int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab),fileid)

#from urllib.request import urlopen
import requests
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
#rawtext = str(urlopen(url).read())
raw = requests.get(url)
type(raw)

rawtext = raw.text

type(rawtext)
#<class 'str'>

len(rawtext)
# 1176968

tokens = nltk.word_tokenize(rawtext)
type(tokens)
#<type 'list'>

len(tokens)
#257727

tokens[:10]
#['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Crime', 'and', 'Punishment', ',', 'by']

text = nltk.Text(tokens)

type(text)
#<class 'nltk.text.Text'>

text[1020:1060]
text[100:200]

# collocations =>  identifying phrases that act like single words in Natural Language Processing.
text.collocations()