from nltk.corpus import reuters

files = reuters.fileids()
print(files)

words16097 = reuters.words(['test/16097'])
print(words16097)

words20 = reuters.words(['test/16097'])[:20]
print(words20)

# output the list of topics
reutersGenres = reuters.categories()
print(reutersGenres)

# Print two categories and print newline if ends with .
for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ',end='')
    if(w is '.'):
        print('')