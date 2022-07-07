import re

import pytest

from write_tight.src.default_patterns import ambiguous_pronouns


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("https://ebolle.github.io/write-tight/styles.css", []),
        ("git it thatthere this THOSE", ["it", "this", "THOSE"]),
    ],
)
def test_ambiguous_pronouns_word_boundaries(test_input: str, expected: str):
    """Test my understanding of the pattern after persistent errors."""
    assert re.findall(ambiguous_pronouns.pattern, test_input) == expected
