const patterns = {
  "ambiguous-pronouns": "#F692BC",
  "ambiguous-openings": "#F4ADC6",
  "words-ending-with-ly": "#FDFD95",
  "subjunctive-mood": "#AAC5E2",
  "passive-voice": "#6891C3",
};

for (pattern in patterns) {
  class_element = document.getElementsByClassName(pattern);

  for (item of class_element) {
    item.style.backgroundColor = patterns[pattern];
  }
}
