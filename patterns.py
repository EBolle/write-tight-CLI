import re

import patterns_utils

def ly(html_content: str) -> str:
    """
    Adds a span element with a 'ly-pattern' class to all words ending on 'ly'.
    """
    ly_pattern = re.compile(r'\w+ly\b')    
    matches = set(re.findall(ly_pattern, html_content))

    matches_dict = patterns_utils.create_span_dict(matches, 'ly-pattern')

    return_html = html_content
    for key, value in matches_dict.items():
        return_html = return_html.replace(key, value)

    return return_html