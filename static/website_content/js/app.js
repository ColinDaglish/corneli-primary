function toggleNavigation() {
    var x = document.querySelector("nav ul");
    if (x.style.display === "none" || x.style.display === ""){
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
