const toggleButton = document.getElementsByClassName('h-toggle-button')[0]
const navBar = document.getElementsByClassName('h-navigation')[0]

toggleButton.addEventListener("click", function(){
  navBar.classList.toggle('active');
});