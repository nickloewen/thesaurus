# Thesaurus

This script replaces words from the text given to it with their synonyms, according to a permutation method chosen by the user.

**Requires [NLTK](http://www.nltk.org/) and the Wordnet corpus (run `nltk.download()` from the interpreter to download WN).**

## Example (change-from-end method)

    > a place of mind

    A place of mind.
    A place of head.
    A place of brain.
    A place of psyche.
    A place of nous.
    A place of judgment.
    A place of judgement.
    A place of thinker.
    A place of creative thinker.
    A place of idea.
    A place of intellect.
    A place of take care.
    A place of heed.
    A place of listen.
    A place of beware.
    A place of bear in mind.
    A topographic point of bear in mind.
    A spot of bear in mind.
    A property of bear in mind.
    A stead of bear in mind.
    A position of bear in mind.
    A lieu of bear in mind.
    A shoes of bear in mind.
    A home of bear in mind.
    A post of bear in mind.
    A berth of bear in mind.
    A office of bear in mind.
    A billet of bear in mind.
    A situation of bear in mind.
    A station of bear in mind.
    A seat of bear in mind.
    A plaza of bear in mind.
    A piazza of bear in mind.
    A space of bear in mind.
    A blank space of bear in mind.
    A put of bear in mind.
    A set of bear in mind.
    A pose of bear in mind.
    A lay of bear in mind.
    A rate of bear in mind.
    A rank of bear in mind.
    A range of bear in mind.
    A order of bear in mind.
    A grade of bear in mind.
    A locate of bear in mind.
    A site of bear in mind.
    A come in of bear in mind.
    A come out of bear in mind.
    A target of bear in mind.
    A aim of bear in mind.
    A direct of bear in mind.
    A point of bear in mind.
    A identify of bear in mind.
    A localize of bear in mind.
    A localise of bear in mind.
    A invest of bear in mind.
    A commit of bear in mind.
    A send of bear in mind.

## Design Idea

The program takes in input, permutes it, then returns the output. Regardless of what approach is taken to permutation, the input and output steps are the same. The goal, therefore, is to construct a system where the input and output code is provided, and the permutation code easily slots in, so it can be created by anyone, without too much knowledge of (or adjustment to) the rest of the program.

## To Do

* actually print each output for the all-possibilities permutation
* allow limiting number of results
    * by hard-coded number (ie, "first 10")
    * by closeness of synonym to original word (see the [WordNet Interface guide](http://www.nltk.org/howto/wordnet.html) for reference)

## Notes

* you must always be able to trust that the first synonyms returned by the create_synonyms functions are the original words

## Resources

* [basic thesaurus script](http://stackoverflow.com/questions/5534926/to-find-synonyms-defintions-and-example-sentences-using-wordnet)
