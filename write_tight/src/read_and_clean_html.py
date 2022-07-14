import re

import requests
from bs4 import BeautifulSoup

import write_tight.src.config as config


class GetHtmlContent:
    def __init__(self, url: str) -> None:
        self.url = url
        self.tag_pattern = re.compile(r"(<\w+)(?:\s+[^>]*)(>)")

    def main(self) -> str:
        """Runs several methods to read, clean, and transform the
        raw html content from the url into a string with HTML content.
        """
        html_raw = self.read_url()
        html_content = self.filter_tags(html_raw)
        html_content = self.remove_tag_content(html_content)

        return html_content

    def read_url(self) -> BeautifulSoup:
        html_raw = requests.get(self.url)

        if html_raw.status_code == 200:
            return BeautifulSoup(html_raw.text, "html.parser")
        else:
            raise ValueError(
                f"The HTML response is not OK: {html_raw.status_code}"
            )

    def filter_tags(self, html_text: BeautifulSoup) -> str:
        html_content = html_text.find_all(config.TAGS)

        return " ".join(str(tag) for tag in html_content)

    def remove_tag_content(self, html_content: str) -> str:
        """Removes all content within tags such as classes and ids to prevent
        potential CSS conflicts.
        """
        return re.sub(self.tag_pattern, r"\1\2", html_content)
