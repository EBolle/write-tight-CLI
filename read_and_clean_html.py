from pathlib import Path
import re

from bs4 import BeautifulSoup
import requests


def main(url: str) -> str:
    """
    Runs several helper functions to read, clean, and transform the
    raw html content of an url into a string with HTML code.
    """
    html_content = read_url(url)
    html_content = filter_tags(html_content)
    html_content = remove_tag_content(html_content)
    html_content = add_js_script_reference(html_content)

    return html_content
    
def read_url(url: str) -> BeautifulSoup:
    """ 
    Processes the url to a BeatifulSoup object which holds 
    the text of the HTML.
    """
    raw_html = requests.get(url)

    if raw_html.status_code == 200:
        return BeautifulSoup(raw_html.text, 'html.parser')
    else:
        raise ValueError(f"The HTML response is not OK: {raw_html.status_code}")

def filter_tags(html_text: BeautifulSoup) -> str:
    """
    Filters the 'h1' and 'p' elements of the BeatifulSoup object and 
    transforms the tags to strings.
    """
    html_content = html_text.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul'])
    html_content_as_str = [str(tag) for tag in html_content]

    return ' '.join(html_content_as_str)

def remove_tag_content(html_content: str) -> str:
    """ 
    Removes all content in chosen HTML tags like classes and ids to keep the tags clean 
    and ready to be modified with this projects` CSS classes. 
    * The sub method is leveraged by only keeping group matches 1 and 4 of the tag_content_pattern.
    """
    tag_content_pattern = re.compile(r'(<(a|p|ol|ul|li|h1|h2|h3|h4|h5|h6))(\s+[^>]*)(>)')

    return re.sub(tag_content_pattern, r'\1\4', html_content)

def add_js_script_reference(html_content :str) -> str:
    """
    Adds the body element to the HTML content with a reference to the JavaScript script.
    """
    current_working_directory = str(Path.cwd())
    body_end = f"""<script src="{current_working_directory}/static/js/script.js"></script>
    </body>"""

    return "<body>" + html_content + body_end