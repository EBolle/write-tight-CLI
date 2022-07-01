import re
from abc import ABC, abstractmethod


class Pattern(ABC):
    @abstractmethod
    def __init__(self, name: str, pattern: re.Pattern):
        self.name = name
        self.pattern = pattern

    @abstractmethod
    def match_and_replace(self, html_content: str) -> str:
        pass

    @abstractmethod
    def add_span_element(self, html_content: str) -> set:
        pass
