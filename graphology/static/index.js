// document.addEventListener("DOMContentLoaded", function() {
//     var navLinks = document.querySelectorAll("nav a");
  
//     navLinks.forEach(function(link) {
//       link.addEventListener("click", function(event) {
//         event.preventDefault();
//         var targetSection = document.querySelector(this.getAttribute("href"));
  
//         if (isElementFullyVisible(targetSection)) {
//           // Section is fully visible, no need to scroll
//           return;
//         }
  
//         targetSection.scrollIntoView({ behavior: "smooth", block: "start" });
//       });
//     });
  
//     function isElementFullyVisible(element) {
//       var rect = element.getBoundingClientRect();
//       return (
//         rect.top >= 0 &&  rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)
//       );
//     }
//   });

  function animateOnScroll() {
    var elements = document.getElementsByClassName('word-animation');
    
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      var position = element.getBoundingClientRect().top;
      var windowHeight = window.innerHeight;
      
      if (position < windowHeight) {
        element.classList.add('animate');
      }
    }
  }
  
  window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.navbar');
    if (window.scrollY > 0) {
      navbar.classList.add('visible');
    } else {
      navbar.classList.remove('visible');
    }
  });
  