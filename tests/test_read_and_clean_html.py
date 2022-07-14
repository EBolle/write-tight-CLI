import re

import pytest

from write_tight.src.read_and_clean_html import GetHtmlContent


@pytest.fixture
def sample_text() -> str:
    text = """<h1 thistextshouldberemoved>and this text should not,
    basically all characters between <p class=certain-elements> but
    what about fictive tags like <lolly what about spaces>?
    """
    return text


@pytest.fixture
def ghc_instance() -> GetHtmlContent:
    ghc_instance = GetHtmlContent(url="")
    return ghc_instance


def test_remove_tag_pattern_matches(
    sample_text: str, ghc_instance: GetHtmlContent
):
    test_input = re.findall(ghc_instance.tag_pattern, sample_text)
    expected = [("<h1", ">"), ("<p", ">"), ("<lolly", ">")]

    assert test_input == expected


def test_remove_tag_pattern_sub(
    sample_text: str, ghc_instance: GetHtmlContent
):
    test_input = re.sub(ghc_instance.tag_pattern, r"\1\2", sample_text)
    expected = """<h1>and this text should not,
    basically all characters between <p> but
    what about fictive tags like <lolly>?
    """

    assert test_input == expected
