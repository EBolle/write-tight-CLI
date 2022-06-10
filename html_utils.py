from bs4 import BeautifulSoup
import requests


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
    html_content = html_text.find_all(['h1', 'p'])
    html_content_as_str = [str(tag) for tag in html_content]

    return ' '.join(html_content_as_str)