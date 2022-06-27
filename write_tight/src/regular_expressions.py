import re
from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    pattern: re.Pattern

    def main(self, html_content: str) -> str:
        matches = self.match(html_content)
        print(matches)
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
    name: str = "ly-pattern"
    pattern: re.Pattern = re.compile(r"\w+ly\b")


@dataclass
class SubjunctiveMoodPattern(Pattern):
    name: str = "sm-pattern"
    pattern: re.Pattern = re.compile(
        r"\b(would|should|could)\b", flags=re.IGNORECASE
    )


words_that_end_on_ly = re.compile(r"\w+ly\b")
subjunctive_mood = re.compile(r"\b(would|should|could)\b", flags=re.IGNORECASE)
passive_voice = re.compile(
    r"\b(am|are|is|was|were|been|being)\b\s{1}(.+?)\b",
    flags=re.IGNORECASE | re.DOTALL,
)


patterns = [
    (words_that_end_on_ly, "ly-pattern"),
    (subjunctive_mood, "sm-pattern"),
    (passive_voice, "pv-pattern"),
]
