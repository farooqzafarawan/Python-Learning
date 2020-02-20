import nltk
from nltk.corpus import brown

print(brown.categories())

genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']

for i in range(0,len(genres)):
    genre = genres[i]
    print()
    print("Analysing '"+ genre + "' wh words")
    genre_text = brown.words(categories = genre)

    # FreqDist() accepts a list of words and returns an 
    # object that contains the map word and its respective frequency in the input word list
    fdist = nltk.FreqDist(genre_text)

    # access fdist object returned by FreqDist() and get count of each of wh words
    for wh in whwords:
        print(wh + ':', fdist[wh], end=' ')

