import re


def main(html_content: str,
         regex: re.Pattern,
         regex_name: str) -> dict[str, set]:
    """Matches each regular expression on the html_content and saves unique
    matches in a dictionary.
    """
    matches = dict()
    matches[regex_name] = set(re.findall(regex, html_content))

    return matches
