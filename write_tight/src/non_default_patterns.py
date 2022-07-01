"""These patterns need additional logic but adhere to
the same Pattern interface.
"""


import re

from nltk.corpus import wordnet as wn

from write_tight.src.pattern import Pattern


class PassiveVoicePattern(Pattern):
    def __init__(self, name: str, pattern: re.Pattern):
        super().__init__(name, pattern)

    def match_and_replace(self, html_content: str) -> str:
        print(html_content)
        return re.sub(self.pattern, self.add_span_element, html_content)

    def add_span_element(self, match: re.Match) -> str:
        match = match.group()
        return self.validate(match)

    def validate(self, match_words: str) -> str:
        """Only keep the matches of which the second word of the match
        is a verb.
        """
        print(match_words)
        second_word = match_words.split()[1]

        if self.is_verb(second_word):
            return f"<span class='{self.name}'>{match_words}</span>"
        else:
            return match_words

    def is_verb(self, word: str) -> bool:
        return bool(wn.synsets(word, pos=wn.VERB))


passive_voice = PassiveVoicePattern(
    name="passive-voice",
    pattern=re.compile(
        r"\b(am|are|is|was|were|been|being)\b\s{1}(.+?)\b",
        flags=re.IGNORECASE | re.DOTALL,
    ),
)
