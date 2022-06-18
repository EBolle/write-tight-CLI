from pathlib import Path
from re import I
import time

import click

from regular_expressions import regular_expressions
from validation import validations
import regular_expressions
import matches
import read_and_clean_html
import search_and_replace


@click.command()
@click.argument('url', type=click.STRING)
def wt(url):
    """
    Opens a new browser tab with the text content of the url and color-coded 
    suggestions on how to improve the text to write tight (wt).
    """
    html_content = read_and_clean_html.main(url)

    for regex in regular_expressions.regular_expressions:
        match = matches.main(html_content, regex)
        if regex[1] in validations:
            regex_name = regex[1]
            regex_matches = match[regex_name]
            match[regex_name] = validations[regex_name](regex_matches)
        html_content = search_and_replace.main(html_content, match)
    
    Path('_temp.html').touch()
    with open('_temp.html', mode='w') as output:
        output.write(html_content)
        click.launch('_temp.html')
        time.sleep(0.5)

    Path('_temp.html').unlink()

if __name__ == '__main__':
    wt()