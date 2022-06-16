"""
The matches of some regular expressions need to be validated before
they are wrapped and replaced in span elements.
"""
from itertools import compress

from nltk.corpus import wordnet as wn


def pv_validation(pv_matches: set) -> set:
    """
    Only keep the matches of which the second word of the match
    is a verb.
    """
    second_word = [words[1] for words in pv_matches]
    is_verb_list = [is_verb(word) for word in second_word]
    
    return set(list(compress(pv_matches, is_verb_list)))

def is_verb(word):
    return bool(wn.synsets(word, pos=wn.VERB))
