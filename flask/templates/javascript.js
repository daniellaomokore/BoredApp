window.onload = function() {
  let clickCount = 0;

  document.getElementById("backButton").addEventListener("click", function() {
    clickCount++;
    history.go(-clickCount);
  });
};
