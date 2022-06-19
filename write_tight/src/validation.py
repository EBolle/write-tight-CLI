"""
The matches of some regular expressions need to be validated before
they are wrapped and replaced in span elements.
"""
from itertools import compress

from nltk.corpus import wordnet as wn


def pv_validation(pv_matches: set[tuple]) -> set[str]:
    """
    Only keep the matches of which the second word of the match
    is a verb. The format string is necessary to get the text back
    to its original form instead of a tuple ('w1', 'w2').
    """
    second_word = [words[1] for words in pv_matches]
    is_verb_matches = [is_verb(word) for word in second_word]
    is_verb_matches = list(compress(pv_matches, is_verb_matches))

    return set([f"{w1} {w2}" for w1, w2 in is_verb_matches])


def is_verb(word: str) -> bool:
    return bool(wn.synsets(word, pos=wn.VERB))


validations = {'pv-pattern': pv_validation}
