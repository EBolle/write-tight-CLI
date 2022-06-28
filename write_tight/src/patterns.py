import re
from dataclasses import dataclass
from itertools import compress

from nltk.corpus import wordnet as wn


class Pattern:
    def __init__(self, name: str, pattern: re.Pattern):
        self.name = name
        self.pattern = pattern

    def main(self, html_content: str) -> str:
        matches = self.match(html_content)
        replaced_html = self.search_and_replace(html_content, matches)

        return replaced_html

    def match(self, html_content: str) -> set:
        return set(re.findall(self.pattern, html_content))

    def search_and_replace(self, html_content: str, matches: set) -> str:
        for match in matches:
            html_content = html_content.replace(
                match, self._add_span_element(match)
            )

        return html_content

    def _add_span_element(self, match: str):
        return f"<span class='{self.name}'>{match}</span>"


@dataclass
class LyPattern(Pattern):
    name = "ly-pattern"
    pattern = re.compile(r"\w+ly\b")


@dataclass
class SubjunctiveMoodPattern(Pattern):
    name = "sm-pattern"
    pattern = re.compile(r"\b(would|should|could)\b", flags=re.IGNORECASE)


@dataclass
class PassiveVoicePattern(Pattern):
    name = "pv-pattern"
    pattern = re.compile(
        r"\b(am|are|is|was|were|been|being)\b\s{1}(.+?)\b",
        flags=re.IGNORECASE | re.DOTALL,
    )

    def main(self, html_content: str) -> str:
        matches = self.match(html_content)
        validated_matches = self.validate(matches)
        replaced_html = self.search_and_replace(
            html_content, validated_matches
        )

        return replaced_html

    def validate(self, matches: set[tuple]) -> set[str]:
        """Only keep the matches of which the second word of the match
        is a verb. The format string is necessary to get the text back
        to its original form instead of a tuple ('w1', 'w2').
        """
        second_word = [words[1] for words in matches]
        is_verb_matches = [self.is_verb(word) for word in second_word]
        is_verb_matches = list(compress(matches, is_verb_matches))

        return set([f"{w1} {w2}" for w1, w2 in is_verb_matches])

    def is_verb(self, word: str) -> bool:
        return bool(wn.synsets(word, pos=wn.VERB))
