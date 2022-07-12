"use strict";

const patterns = {
  "ambiguous-openings": "#ffd8b1",
  "ambiguous-pronouns": "#fabed4",
  "passive-voice": "#fffac8",
  "subjunctive-mood": "#42d4f4",
  "words-ending-with-ly": "#aaffc3",
};

for (let pattern in patterns) {
  let spanElements = document.querySelectorAll(`span[class=${pattern}]`);
  let liElement = document.querySelectorAll(`li[class=${pattern}]`);

  if (spanElements.length === 0) {
    liElement[0].classList.add(`hidden`);
  } else {
    liElement[0].style.color = patterns[pattern];

    for (let item of spanElements) {
      item.style.backgroundColor = patterns[pattern];
    }
  }
}
