import click

from write_tight.src.add_html import AddHtml
from write_tight.src.launch_html import launch_html
from write_tight.src.read_and_clean_html import GetHtmlContent
from write_tight.src.default_patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    words_ending_with_ly,
    subjunctive_mood,
)
from write_tight.src.non_default_patterns import passive_voice


patterns = [
    ambiguous_pronouns,
    ambiguous_openings,
    words_ending_with_ly,
    subjunctive_mood,
    passive_voice,
]


@click.command()
@click.argument("url", type=click.STRING)
def wt(url: str):
    """Opens a new browser tab with the text content of the url and color-coded
    suggestions on how to improve the text to write tight (wt).
    """
    html_content = GetHtmlContent(url).main()

    for pattern in patterns:
        html_content = pattern.match_and_replace(html_content)

    html_content = AddHtml(html_content).main()

    launch_html(html_content)


if __name__ == "__main__":
    wt()
