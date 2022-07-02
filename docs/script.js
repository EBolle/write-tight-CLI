// The colors need to have high contrast since there can be lots of color highlighting
// in close proximity. Hence I have used this blog for assistance: https://sashamaps.net/docs/resources/20-colors/.

const patterns = {
  "ambiguous-pronouns": "#469990",
  "ambiguous-openings": "#ffd8b1",
  "words-ending-with-ly": "#aaffc3",
  "subjunctive-mood": "#42d4f4",
  "passive-voice": "#e6194B",
};

for (pattern in patterns) {
  class_element = document.getElementsByClassName(pattern);

  for (item of class_element) {
    item.style.backgroundColor = patterns[pattern];
  }
}
