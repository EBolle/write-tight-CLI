import re

import requests
from bs4 import BeautifulSoup

import write_tight.src.config as config


class GetHtmlContent:
    def __init__(self, url: str) -> None:
        self.url = url

    def main(self) -> str:
        """Runs several methods to read, clean, and transform the
        raw html content from the url into a string with HTML content.
        """
        html_raw = self.read_url()
        html_content = self.filter_tags(html_raw)
        html_content = self.remove_tag_content(html_content)
        html_content = self.add_js_script_reference(html_content)
        html_content = self.add_css_script_reference(html_content)

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
        pattern_string = rf"(<({'|'.join(config.TAGS)}))(\s+[^>]*)(>)"
        tag_pattern = re.compile(pattern_string)

        return re.sub(tag_pattern, r"\1\4", html_content)

    def add_js_script_reference(self, html_content: str) -> str:
        body_start = "<body>"
        body_end = f"""<script src={config.JS_URL}></script>
        </body>"""

        return body_start + html_content + body_end

    def add_css_script_reference(self, html_content: str) -> str:
        head = f"""
        <head>
        <link rel="stylesheet" href="{config.CSS_URL}">
        </head>"""

        return head + html_content
