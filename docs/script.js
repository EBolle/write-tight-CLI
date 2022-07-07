// The colors need to have high contrast since there can be lots of color highlighting
// in close proximity. Hence I have used this blog for assistance: https://sashamaps.net/docs/resources/20-colors/.

const patterns = {
  "ambiguous-openings": "#ffd8b1",
  "ambiguous-pronouns": "#fabed4",
  "passive-voice": "#fffac8",
  "subjunctive-mood": "#42d4f4",
  "words-ending-with-ly": "#aaffc3",
};

for (let pattern in patterns) {
  span_elements = document.querySelectorAll(`span[class=${pattern}]`);
  li_element = document.querySelectorAll(`li[class=${pattern}]`);

  if (span_elements.length === 0) {
    li_element[0].classList.add(`hidden`);
  } else {
    li_element[0].style.color = patterns[pattern];

    for (let item of span_elements) {
      item.style.backgroundColor = patterns[pattern];
    }
  }
}
