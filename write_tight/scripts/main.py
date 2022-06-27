import time
from pathlib import Path

import click

from write_tight.src.read_and_clean_html import GetHtmlContent
from write_tight.src.regular_expressions import (
    LyPattern,
    SubjunctiveMoodPattern,
)


patterns = [LyPattern, SubjunctiveMoodPattern]


@click.command()
@click.argument("url", type=click.STRING)
def wt(url):
    """Opens a new browser tab with the text content of the url and color-coded
    suggestions on how to improve the text to write tight (wt).
    """
    get_html_content = GetHtmlContent(url)
    html_content = get_html_content.main(url)

    for pattern in patterns:
        html_content = pattern().main(html_content)

    Path("_temp.html").touch()
    with open("_temp.html", mode="w") as output:
        output.write(html_content)
        click.launch("_temp.html")
        time.sleep(0.5)

    Path("_temp.html").unlink()


if __name__ == "__main__":
    wt()
