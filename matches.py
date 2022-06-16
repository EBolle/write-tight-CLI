import re 


def main(html_content: str, regular_expressions_list: list) -> dict:
    """
    Matches each regular expression on the html_content and saves unique
    matches in a dictionary.
    """
    match_dict = dict()

    for regular_expression in regular_expressions_list:
        match_set = set(re.findall(regular_expression[0], html_content))
        match_dict[regular_expression[1]] = match_set

    return match_dict
