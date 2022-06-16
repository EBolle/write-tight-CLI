"""
The matches of some regular expressions need to be validated before
they are wrapped and replaced in span elements.
"""
from itertools import compress

from nltk.corpus import wordnet as wn


def pv_validation(pv_matches: set) -> set:
    """
    Only keep the matches of which the second word of the match
    is a verb. The format string is necessary to get the text back
    to its original form instead of a tuple ('w1', 'w2').
    """
    second_word = [words[1] for words in pv_matches]
    is_verb_list = [is_verb(word) for word in second_word]
    to_keep_list = list(compress(pv_matches, is_verb_list))

    return set([f"{w1} {w2}" for w1, w2 in to_keep_list])


def is_verb(word):
    return bool(wn.synsets(word, pos=wn.VERB))
