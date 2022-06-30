import re
from abc import ABC, abstractmethod


class Pattern(ABC):
    @abstractmethod
    def __init__(self, name: str, pattern: re.Pattern):
        self.name = name
        self.pattern = pattern

    @abstractmethod
    def main(self, html_content: str) -> str:
        pass

    @abstractmethod
    def match(self, html_content: str) -> set:
        pass

    @abstractmethod
    def search_and_replace(self, html_content: str, matches: set) -> str:
        pass
