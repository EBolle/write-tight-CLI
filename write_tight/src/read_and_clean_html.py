from dataclasses import dataclass
from pathlib import Path
import re

from bs4 import BeautifulSoup
import requests


current_working_directory = str(Path.cwd())


@dataclass
class GetHtmlContent:
    url: str
    JS_URL: str = f"{current_working_directory}/static/js/script.js"
    CSS_URL: str = f"{current_working_directory}/static/css/styles.css"

    def main(self, url: str) -> str:
        """Runs several helper functions to read, clean, and transform the
        raw html content from the url into a string with HTML content.
        """
        html_content = self.read_url(url)
        html_content = self.filter_tags(html_content)
        html_content = self.remove_tag_content(html_content)
        html_content = self.add_js_script_reference(html_content)
        html_content = self.add_css_script_reference(html_content)

        return html_content

    @staticmethod
    def read_url(url: str) -> BeautifulSoup:
        raw_html = requests.get(url)

        if raw_html.status_code == 200:
            return BeautifulSoup(raw_html.text, 'html.parser')
        else:
            raise ValueError(
                f"The HTML response is not OK: {raw_html.status_code}"
            )

    def filter_tags(self, html_text: BeautifulSoup) -> str:
        html_content = html_text.find_all(['h1', 'h2', 'h3', 'h4', 'h5',
                                           'h6', 'p', 'ol', 'ul'])

        return ' '.join(str(tag) for tag in html_content)

    def remove_tag_content(self, html_content: str) -> str:
        tag_content_pattern = re.compile(
            r'(<(a|p|ol|ul|li|h1|h2|h3|h4|h5|h6))(\s+[^>]*)(>)'
        )

        return re.sub(tag_content_pattern, r'\1\4', html_content)

    def add_js_script_reference(self, html_content: str) -> str:
        body_start = "<body>"
        body_end = f"""
        <script src={self.JS_URL}></script>
        </body>"""

        return body_start + html_content + body_end

    def add_css_script_reference(self, html_content: str) -> str:
        head = f"""
        <head>
        <link rel="stylesheet"
        href="{self.CSS_URL}">
        </head>"""

        return head + html_content
