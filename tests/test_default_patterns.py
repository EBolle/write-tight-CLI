from write_tight.src.default_patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    words_ending_with_ly,
    subjunctive_mood,
)


def test_ambiguous_pronouns_0():
    result = ambiguous_pronouns.match(
        "https://ebolle.github.io/write-tight/styles.css"
    )
    expected = set()

    assert result == expected


def test_ambiguous_pronouns_1():
    result = ambiguous_pronouns.match("git it thatthere this THOSE")
    expected = set(["it", "this", "THOSE"])

    assert result == expected


def test_ambiguous_pronouns_2():
    result = ambiguous_pronouns.match(
        '<link rel="stylesheet"'
        ' href="https://ebolle.github.io/write-tight/styles.css">'
    )
    expected = set()

    assert result == expected
