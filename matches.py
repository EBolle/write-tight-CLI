import re 


def main(html_content: str, regular_expression: tuple) -> dict[str, set]:
    """
    Matches each regular expression on the html_content and saves unique
    matches in a dictionary.
    """
    matches = dict()
    matches[regular_expression[1]] = set(re.findall(regular_expression[0], html_content))

    return matches
