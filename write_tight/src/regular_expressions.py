import re
from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    pattern: re.Pattern
    html_content: str

    def main(self) -> str:
        matches = self.match()
        replaced_html = self.search_and_replace(matches)

        return replaced_html

    def match(self) -> set:
        return set(re.findall(self.pattern, self.html_content))

    def search_and_replace(self, matches: set) -> str:
        return_html = self.html_content

        for match in matches:
            return_html.replace(match, self._add_span_element(match))

        return return_html

    def _add_span_element(self, match: str):
        return f"<span class='{self.name}'>{match}</span>"


words_that_end_on_ly = re.compile(r'\w+ly\b')
subjunctive_mood = re.compile(r'\b(would|should|could)\b', flags=re.IGNORECASE)
passive_voice = re.compile(
    r'\b(am|are|is|was|were|been|being)\b\s{1}(.+?)\b',
    flags=re.IGNORECASE | re.DOTALL
)


patterns = [(words_that_end_on_ly, 'ly-pattern'),
            (subjunctive_mood, 'sm-pattern'),
            (passive_voice, 'pv-pattern')]
