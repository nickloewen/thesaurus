# Notes

## Design Idea

The program takes in input, permutes it, then returns the output. Regardless of what approach is taken to permutation, the input and output steps are the same. The goal, therefore, is to construct a system where the input and output code is provided, and the permutation code easily slots in, so it can be created by anyone, without too much knowledge of (or adjustment to) the rest of the program.

## To Do

* actually print each output for the all-possibilities permutation
* allow limiting number of results
    * by hard-coded number (ie, "first 10")
    * by closeness of synonym to original word (see the [WordNet Interface guide](http://www.nltk.org/howto/wordnet.html) for reference)

## Misc. notes

* you must always be able to trust that the first synonyms returned by the create_synonyms functions are the original words

## Resources

* [basic thesaurus script](http://stackoverflow.com/questions/5534926/to-find-synonyms-defintions-and-example-sentences-using-wordnet)
