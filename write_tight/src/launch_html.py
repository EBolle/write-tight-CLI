import time
from pathlib import Path

import click
from jinja2 import Environment, PackageLoader, select_autoescape
from markupsafe import Markup

import write_tight.src.config as config


env = Environment(
    loader=PackageLoader("write_tight"), autoescape=select_autoescape()
)
post_template = env.get_template("post.html")


def launch_html(html_content: str) -> None:
    Path("_temp.html").touch()

    with open("_temp.html", mode="w") as output:
        output.write(
            post_template.render(
                css_link=config.CSS_URL,
                content=Markup(html_content),
                js_link=config.JS_URL,
            )
        )
        click.launch("_temp.html")
        time.sleep(0.5)

    Path("_temp.html").unlink()
