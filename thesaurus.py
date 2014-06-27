import nltk
from nltk.corpus import wordnet
#from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.tokenize import RegexpTokenizer

def create_word_synonyms(word):
    synsets = wordnet.synsets(word)
    synonyms = []

    for s in synsets:
        for l in s.lemmas:
            synonyms.append(l.name)

    # if there are no synonyms, put the original word in
    if not synsets:
        synonyms.append(word)

    # make token_synonyms a set to remove duplicates
    synonyms = set(synonyms)
    # put it back again
    synonyms = list(synonyms)

    return synonyms

def create_phrase_synonyms(input):
    """Finds synonyms for every word in the input. Returns a list, containing a
    list of synonyms for every word in the input."""

    #tokens = PunktWordTokenizer().tokenize(input)
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    tokens = tokenizer.tokenize(input)

    # synonyms for all words: each word is a list of synonyms inside this one
    synonyms = []

    for t in tokens:
        synonyms.append(create_word_synonyms(t))

    return synonyms


def create_random_synonym_phrases(phrase_synonyms):
    output = []

    """Determine which token has the most phrase_synonyms."""
    longest = ""
    for item in phrase_synonyms:
        if len(item) > len(longest):
            longest = item

    # Loop for each synonym in 'longest' list.

    for i in range(len(longest)):
        """Build a new phrase using the first word of each list, then remove
           that word, unless it is the last one."""

        phrase = ""
        for s in phrase_synonyms:
            phrase = phrase + " " + s[0]

            if len(s) > 1:
                s.pop(0)
        output.append(phrase)

    return output

while True:
    input = raw_input("> ")
    print

    output = create_phrase_synonyms(input)
    output = create_random_synonym_phrases(output)

    for phrase in output:
        print phrase
