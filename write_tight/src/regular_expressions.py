import re


words_that_end_on_ly = re.compile(r'\w+ly\b')
subjunctive_mood = re.compile(r'\b(would|should|could)\b', flags=re.IGNORECASE)
passive_voice = re.compile(
    r'\b(am|are|is|was|were|been|being)\b\s{1}(.+?)\b',
    flags=re.IGNORECASE | re.DOTALL
)


patterns = [(words_that_end_on_ly, 'ly-pattern'),
            (subjunctive_mood, 'sm-pattern'),
            (passive_voice, 'pv-pattern')]