

def main(html_content: str, match_dict: dict) -> str:
    """ 
    Search and replace all matches of all patterns with span elements
    including a class reference to the regular expressions.
    """
    for pattern, match_set in match_dict.items():
        for match in match_set:
            html_content = html_content.replace(match, add_span_element(match, pattern))

    return html_content


def add_span_element(match: str, class_name: str) -> dict:
    """
    Wraps the match in a <span> element including the class name.
    """
    return f"<span class='{class_name}'>{match}</span>"
