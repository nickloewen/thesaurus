# Thesaurus

Quick script that takes raw input and replaces each word with a synonym.

## Example

    > a place of mind

    A set of judgement
    a shoes of head
    type_A office of take_care
    deoxyadenosine_monophosphate point of creative_thinker
    adenine grade of beware
    vitamin_A commit of mind
    antiophthalmic_factor site of idea
    angstrom_unit rank of psyche
    group_A seat of brain
    angstrom rate of thinker
    amp identify of heed
    ampere blank_space of bear_in_mind
    axerophthol lieu of nous
    axerophthol home of judgment
    axerophthol come_out of intellect
    axerophthol space of listen
    axerophthol localise of listen
    axerophthol send of listen
    axerophthol station of listen
    axerophthol place of listen
    axerophthol topographic_point of listen
    axerophthol locate of listen

## Resources

* [basic thesaurus script](http://stackoverflow.com/questions/5534926/to-find-synonyms-defintions-and-example-sentences-using-wordnet)

### Stuff to Implement

* potentially filter out results which are too far from original (see the [WordNet Interface guide](http://www.nltk.org/howto/wordnet.html) for reference)

### To do

* prevent it from changing basic words (a, the, of, in...)

    preserve = ["a", "the", "of", "in"]

    # ...

    if token not in preserve:
        # grab from thesaurus

* strip out underscores
* randomize output?
* actually print each output
* change words starting at end:

    a place of mind
    a place of head
    a place of forehead
    a location of forehead
    a space of forehead
    a vicinity of forehead
