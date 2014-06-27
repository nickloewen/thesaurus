# http://stackoverflow.com/questions/5534926/to-find-synonyms-defintions-and-example-sentences-using-wordnet

import nltk
from nltk.corpus import wordnet
from nltk.tokenize.punkt import PunktWordTokenizer

# http://stackoverflow.com/questions/363944/python-idiom-to-return-first-item-or-none
def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

input = raw_input("> ")

tokens = PunktWordTokenizer().tokenize(input)

# synonyms for all words: each word is a list of synonyms inside this one
synonyms = []

for t in tokens:
    synsets = wordnet.synsets(t)

    """
    Punctuation issues:
    - we get no synonym if the token contains punctuation
    """

    # list to store this token's synonyms in
    token_synonyms = []

    for s in synsets:
        for l in s.lemmas:
            #print l.name
            token_synonyms.append(l.name)

    # if there are no synonyms, put the original word in
    if not synsets:
        token_synonyms.append(t)

    # make token_synonyms a set to remove duplicates
    token_synonyms = set(token_synonyms)
    # put it back again
    token_synonyms = list(token_synonyms)
    synonyms.append(token_synonyms)

#print synonyms

# now re-combine the synonyms...

# figure out which word has the most synonyms

longest = ""
for item in synonyms:
    if len(item) > len(longest):
        longest = item

# loop once for each item in longest

i = 0
while i < len(longest):
    
    # build a new sentence using the first word of each list,
    # then remove that word, unless it is the last one.

    sentence = ""

    for s in synonyms:
        sentence = sentence + " " + s[0]

        if len(s) > 1:
            s.pop(0)

    print sentence

    i += 1
