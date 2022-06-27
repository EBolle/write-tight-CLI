import re
from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    pattern: re.Pattern

    def main(self, html_content: str) -> str:
        matches = self.match(html_content)
        replaced_html = self.search_and_replace(matches)

        return replaced_html

    def match(self, html_content: str) -> set:
        return set(re.findall(self.pattern, self.html_content))

    def search_and_replace(self, matches: set) -> str:
        return_html = self.html_content

        for match in matches:
            return_html.replace(match, self._add_span_element(match))

        return return_html

    def _add_span_element(self, match: str):
        return f"<span class='{self.name}'>{match}</span>"


class LyPattern(Pattern):
    name = 'ly-pattern'
    pattern = re.compile(r'\w+ly\b')


class SubjunctiveMoodPattern(Pattern):
    name = 'sm-pattern'
    pattern = re.compile(r'\b(would|should|could)\b', flags=re.IGNORECASE)


words_that_end_on_ly = re.compile(r'\w+ly\b')
subjunctive_mood = re.compile(r'\b(would|should|could)\b', flags=re.IGNORECASE)
passive_voice = re.compile(
    r'\b(am|are|is|was|were|been|being)\b\s{1}(.+?)\b',
    flags=re.IGNORECASE | re.DOTALL
)


patterns = [(words_that_end_on_ly, 'ly-pattern'),
            (subjunctive_mood, 'sm-pattern'),
            (passive_voice, 'pv-pattern')]
