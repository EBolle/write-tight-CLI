// Retrieve every unique class from all the span elements.
// For each span element apply it's own background color.

const colors = ["orange", "yellow"];
const spans = document.querySelectorAll("span");
const classSet = new Set();

for (span of spans) {
  classSet.add(span.classList.value);
}

const classArray = Array.from(classSet);

for ([index, element] of classArray.entries()) {
  class_element = document.getElementsByClassName(element);
  for (match of class_element) {
    match.style.backgroundColor = colors[index];
  }
}
