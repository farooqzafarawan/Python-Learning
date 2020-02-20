from nltk.corpus import wordnet as wn
chair = 'chair'

chair_synsets = wn.synsets(chair)
print('Synsets/Senses of Chair :', chair_synsets, '\n\n')

# line 1 is name of Synset, line 2 is definition of sense/Synset, 
# line 3 contains Lemmas associated with this Synset, line 4 is an example sentence.
for synset in chair_synsets:
    print(synset, ': ')
    print('Definition: ', synset.definition())
    print('Lemmas/Synonymous words: ', synset.lemma_names())
    print('Example: ', synset.examples(), '\n')