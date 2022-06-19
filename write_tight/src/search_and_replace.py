

def main(html_content: str, match: dict[str, str]) -> str:
    """Search and replace every match with span elements
    including a class reference to the regular expressions name.
    """
    for regex_name, matches in match.items():
        for match in matches:
            html_content = html_content.replace(
                match,
                add_span_element(match, regex_name)
            )

    return html_content


def add_span_element(match: str, regex_name: str) -> str:
    return f"<span class='{regex_name}'>{match}</span>"
