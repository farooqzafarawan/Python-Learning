from nltk.corpus import wordnet as wn
type = 'n'   # n corresponds to nouns

# API returns all synsets of type n that is a noun present in the WordNet database, full coverage
synsets = wn.all_synsets(type)

# consolidate all lemmas in each of the synset into a single mega list
lemmas = []
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

# Use List comprehension to create lemmas list but get all synsets again because generator is empty now
synsets = wn.all_synsets(type)
lemmas2 = [lemma.name() for synset in synsets for lemma in synset.lemmas()]

# remove the duplicates
lemmas = set(lemmas)

# count senses of each lemma in the WordNet database
count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

#  print total distinct lemmas, count of senses, avg polysemy of POS type n or noun
print('Total distinct lemmas: ', len(lemmas))
print('Total senses :',count)
print('Average Polysemy of ', type,': ' , count/len(lemmas))