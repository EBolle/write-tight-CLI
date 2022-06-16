from pathlib import Path
import time

import click 

from regular_expressions import regular_expressions_list
import matches
import read_and_clean_html
import search_and_replace
import validation


@click.command()
@click.argument('url', type=click.STRING)
def wt(url):
    """
    Opens a new browser tab with the text content of the url and color-coded 
    suggestions on how to improve the text to write tight (wt).
    """
    html_content = read_and_clean_html.main(url)

    matches_dict = matches.main(html_content, regular_expressions_list)
    matches_dict['pv-pattern'] = validation.pv_validation(matches_dict['pv-pattern'])

    html_content = search_and_replace.main(html_content, matches_dict)

    Path('_temp.html').touch()
    with open('_temp.html', mode='w') as output:
        output.write(html_content)
        click.launch('_temp.html')
        time.sleep(0.5)

    Path('_temp.html').unlink()

if __name__ == '__main__':
    wt()