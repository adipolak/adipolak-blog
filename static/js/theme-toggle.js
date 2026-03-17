// Dark mode is the only theme - no toggle needed
// The site uses a warm dark editorial design system by default
(function() {
  // Remove any light mode classes if they exist from previous versions
  document.body.classList.remove('light-mode');

  // Clear any saved theme preferences from localStorage
  localStorage.removeItem('theme');
})();
