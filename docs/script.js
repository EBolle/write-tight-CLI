const patterns = {
  "words-ending-with-ly": "#AAC8FA",
  "subjunctive-mood": "#FFCFCF",
  "passive-voice": "#C2E7FF",
};

for (pattern in patterns) {
  class_element = document.getElementsByClassName(pattern);

  for (item of class_element) {
    item.style.backgroundColor = patterns[pattern];
  }
}
