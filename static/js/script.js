console.log("Does this actually work?");

// Add background color for each match for each pattern
const lyMatches = document.getElementsByClassName("ly-pattern");

for (match of lyMatches) {
  match.style.backgroundColor = "orange";
}
