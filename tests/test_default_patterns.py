"""Testing my understanding of the patterns."""
import re

import pytest

from write_tight.src.default_patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("https://ebolle.github.io/write-tight/styles.css", []),
        ("git it thatthere this THOSE", ["it", "this", "THOSE"]),
    ],
)
def test_ambiguous_pronouns_word_boundaries(test_input: str, expected: str):
    assert re.findall(ambiguous_pronouns.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Therefore is this a test.", []),
        ("It was an amazing experience.", [("It", "was")]),
        ("Hi there, it was amazing!", []),
        ("There  are spaces to consider.", []),
    ],
)
def test_ambiguous_openings(test_input: str, expected: str):
    assert re.findall(ambiguous_openings.pattern, test_input) == expected
