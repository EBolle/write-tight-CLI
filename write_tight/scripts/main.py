import click

from write_tight.src.launch_html import launch_html
from write_tight.src.read_and_clean_html import GetHtmlContent
from write_tight.src.pattern_implementation import (
    passive_voice,
    subjunctive_mood,
    words_ending_with_ly,
)


patterns = [
    passive_voice,
    subjunctive_mood,
    words_ending_with_ly,
]


@click.command()
@click.argument("url", type=click.STRING)
def wt(url):
    """Opens a new browser tab with the text content of the url and color-coded
    suggestions on how to improve the text to write tight (wt).
    """
    html_content = GetHtmlContent(url).main()

    for pattern in patterns:
        html_content = pattern.main(html_content)

    launch_html(html_content)


if __name__ == "__main__":
    wt()
