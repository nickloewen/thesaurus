import nltk
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
import re

# TOOLS #######################################################################

# words not to convert to synonyms
words_to_preserve = ["a", "the", "in", "of", "at"]
words_to_preserve.extend([w.title() for w in words_to_preserve])
punctuation = [".", ",", ":", ";", "?", "!"]

def create_word_synonyms(word):
    synsets = wordnet.synsets(word)
    synonyms = [word]

    if word not in words_to_preserve:
        for s in synsets:
            for l in s.lemmas:
                synonyms.append(l.name)

    # if there are no synonyms, put the original word in
    synonyms.append(word)

    return uniq(synonyms)


def create_phrase_synonyms(input):
    """Finds synonyms for every word in the input. Returns a list, containing a
    list of synonyms for every word in the input."""

    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    tokens = tokenizer.tokenize(input)

    # synonyms for all words: each word is a list of synonyms inside this one
    synonyms = []

    for t in tokens:
        synonyms.append(create_word_synonyms(t))

    #print synonyms
    return synonyms


def strip_underscores(word):
    return re.sub("_", " ", word)

def tidy_punctuation(word):
    return re.sub(r'\s([?.!"](?:\s|$))', r'\1', word)

def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

# PERMUTATION ALGORITHMS ######################################################


def permute_all_synonyms(phrase_synonyms):
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


def permute_synonyms_from_end(phrase_synonyms):
    output = []
    phrase = ""

    w = len(phrase_synonyms) - 1
    
    while True:
        phrase = [s[0] for s in phrase_synonyms]
        phrase = " ".join(phrase)
        output.append(phrase)

        if w == 0 and len(phrase_synonyms[w]) == 1:
            break
        elif len(phrase_synonyms[w]) > 1:
            del phrase_synonyms[w][0]
        else:
            w -= 1

    # TODO: figure out why the uniq() is needed here
    return uniq(output)


# OUTPUT ######################################################################

print "Select permutation method:"
print "0 - change from end"
print "1 - change all (beta)"
method = raw_input("> ")

if (method not in ["0", "1"]):
    raise ValueError, "Invalid choice of method"

while True:
    input = raw_input("> ")
    print

    output = create_phrase_synonyms(input)
    if (method == "0"):
        output = permute_synonyms_from_end(output)
    else:
        output = permute_all_synonyms(output)

    for phrase in output:
        print tidy_punctuation(strip_underscores(phrase))
