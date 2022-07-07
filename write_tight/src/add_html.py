import write_tight.src.config as config


class AddHtml:
    def __init__(self, html_content: str):
        self.html_content = html_content

    def main(self) -> str:
        html_content = self.add_navbar(self.html_content)
        html_content = self.add_js_script_reference(html_content)
        html_content = self.add_css_script_reference(html_content)

        return html_content

    def add_js_script_reference(self, html_content: str) -> str:
        body_start = "<body>"
        body_end = f"""<script src={config.JS_URL}></script>
        </body>"""

        return body_start + html_content + body_end

    def add_css_script_reference(self, html_content: str) -> str:
        head = f"""
        <head>
        <link rel="stylesheet" href="{config.CSS_URL}">
        </head>"""

        return head + html_content

    def add_navbar(self, html_content: str) -> str:
        """JS + CSS + THIS method need to go to a separate
        module which is executed after the search_and_replace.
        """
        navbar = """
        <header class="sticky">
        <nav>
            <ul class="nav-bar">
            <li class="ambiguous-openings">
            Ambiguous openings<br />
            There was, It were, It was. These sentence openings are vague. The
            more specific your writing, the more authority your document will
            have.
            </li>
            <li class='ambiguous-pronouns'>
            Ambiguous pronouns<br />
            It, these, those, and that are vague. The more precise your
            writing, the better.
            </li>
            <li class='passive-voice'>
            Passive voice<br />
            Was reading, is happening, are reading. A to be verb followed by a
            verb is an indicator of passive voice. Try to write 90% of your
            document in active voice.
            </li>
            <li class='subjunctive-mood'>
            Subjunctive mood<br />
            Would of, should of, could of. Besides sounding weak, subjunctive
            mood can also suggest a condition when it is not present. This
            can cause confusion.
            </li>
            <li class='words-ending-with-ly'>
            Words that end with ly<br />
            Basically, usually, normally. These words can <em>usually</em> be
            removed from your document without losing any meaning.
            </li>
            </ul>
        </nav>
        </header>
        """

        return navbar + html_content
