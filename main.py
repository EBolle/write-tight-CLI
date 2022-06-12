import click 

import html_utils 

@click.command()
@click.argument('url', type=click.STRING)
def wt(url):
    """
    Opens a new browser tab with the text content of the url and color-coded 
    suggestions how to improve the text to write tight (wt).
    """
    html_text = html_utils.read_url(url)
    html_content = html_utils.filter_tags(html_text)
    html_content = html_utils.remove_tag_content(html_content)

    click.echo(html_content)

if __name__ == '__main__':
    wt()