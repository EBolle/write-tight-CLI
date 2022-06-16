from cgitb import html
import time
from pathlib import Path

import click 

import read_and_clean_html 
import patterns
import patterns_utils

@click.command()
@click.argument('url', type=click.STRING)
def wt(url):
    """
    Opens a new browser tab with the text content of the url and color-coded 
    suggestions on how to improve the text to write tight (wt).
    """
    html_content = read_and_clean_html.main(url)
    
    for pattern in patterns.patterns_list:
        html_content = patterns_utils.match_and_replace(html_content, pattern)

    Path('_temp.html').touch()
    with open('_temp.html', mode='w') as output:
        output.write(html_content)
        click.launch('_temp.html')
        time.sleep(0.5)

    Path('_temp.html').unlink()

if __name__ == '__main__':
    wt()