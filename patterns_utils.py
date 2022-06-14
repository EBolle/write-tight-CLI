import re


def create_span_dict(words: set, class_name: str) -> dict:
    """
    Wraps the words in <span> elements including the class name and stores
    these elements as values. The words are the keys.
    """
    return {word: f"<span class='{class_name}'>{word}</span>" for word in words}


def match_and_replace(html_content: str, pattern: tuple) -> str:
    """
    Replaces all pattern matches in html_content with the matches wrapped in span
    elements including a reference CSS class. 
    """
    matches = set(re.findall(pattern[0], html_content))

    matches_dict = create_span_dict(matches, pattern[1])

    return_html = html_content
    for key, value in matches_dict.items():
        return_html = return_html.replace(key, value)

    return return_html