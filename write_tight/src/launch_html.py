import time
from pathlib import Path

import click


def launch_html(html_content: str) -> None:
    Path("_temp.html").touch()

    with open("_temp.html", mode="w") as output:
        output.write(html_content)
        click.launch("_temp.html")
        time.sleep(0.5)

    Path("_temp.html").unlink()
