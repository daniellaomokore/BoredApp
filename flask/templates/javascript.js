window.onload = function() {
  let clickCount = 0;

  console.log("JavaScript code is running");

  document.getElementById("backButton").addEventListener("click", function() {
    clickCount++;
    console.log("Button was clicked", clickCount);
    history.go(-clickCount);
  });
};