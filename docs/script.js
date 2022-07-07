// The colors need to have high contrast since there can be lots of color highlighting
// in close proximity. Hence I have used this blog for assistance: https://sashamaps.net/docs/resources/20-colors/.

const patterns = {
  "ambiguous-openings": "#ffd8b1",
  "ambiguous-pronouns": "#fabed4",
  "passive-voice": "#fffac8",
  "subjunctive-mood": "#42d4f4",
  "words-ending-with-ly": "#aaffc3",
};

for (pattern in patterns) {
  class_element = document.getElementsByClassName(pattern);

  for (item of class_element) {
    item.style.backgroundColor = patterns[pattern];
  }
}
