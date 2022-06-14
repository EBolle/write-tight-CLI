import time
from pathlib import Path

import click 

import html_utils 
import patterns

@click.command()
@click.argument('url', type=click.STRING)
def wt(url):
    """
    Opens a new browser tab with the text content of the url and color-coded 
    suggestions on how to improve the text to write tight (wt).
    """
    html_text = html_utils.read_url(url)
    html_content = html_utils.filter_tags(html_text)
    html_content = html_utils.remove_tag_content(html_content)
    html_content = html_utils.add_js_script_reference(html_content)

    html_content = patterns.ly(html_content)

    Path('_temp.html').touch()
    with open('_temp.html', mode='w') as output:
        output.write(html_content)
        click.launch('_temp.html')
        time.sleep(0.5)

    # Path('_temp.html').unlink()

if __name__ == '__main__':
    wt()