// Add background color for each match for each pattern
const lyMatches = document.getElementsByClassName("ly-pattern");

for (match of lyMatches) {
  match.style.backgroundColor = "orange";
}

const smMatches = document.getElementsByClassName("sm-pattern");

for (match of smMatches) {
  match.style.backgroundColor = "yellow";
}
