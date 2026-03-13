// Theme toggle functionality - Dark mode as default
(function() {
  console.log('Theme toggle script loaded');

  // Check for saved theme preference, default to dark mode
  const savedTheme = localStorage.getItem('theme');
  const preferredTheme = savedTheme || 'dark';

  console.log('Saved theme:', savedTheme);
  console.log('Preferred theme:', preferredTheme);

  // Apply theme on page load immediately
  if (preferredTheme === 'light') {
    document.body.classList.add('light-mode');
  } else {
    // Dark mode is default, no class needed
    document.body.classList.remove('light-mode');
  }

  // Function to create and add toggle button
  function createToggleButton() {
    // Check if button already exists
    if (document.querySelector('.dark-mode-toggle')) {
      console.log('Toggle button already exists');
      return;
    }

    console.log('Creating theme toggle button');

    // Create theme toggle button
    const toggleButton = document.createElement('button');
    toggleButton.className = 'dark-mode-toggle';
    toggleButton.setAttribute('aria-label', 'Toggle between light and dark mode');
    toggleButton.setAttribute('aria-pressed', preferredTheme === 'dark' ? 'false' : 'true');
    toggleButton.setAttribute('type', 'button');
    toggleButton.innerHTML = preferredTheme === 'light' ? '🌙' : '☀️';

    // Add to body
    document.body.appendChild(toggleButton);
    console.log('Toggle button added to page');

    // Toggle theme on button click
    toggleButton.addEventListener('click', function() {
      console.log('Toggle button clicked');
      document.body.classList.toggle('light-mode');
      const isLight = document.body.classList.contains('light-mode');

      // Update button icon and aria-pressed
      toggleButton.innerHTML = isLight ? '🌙' : '☀️';
      toggleButton.setAttribute('aria-pressed', isLight ? 'true' : 'false');

      // Update aria-label
      toggleButton.setAttribute('aria-label',
        isLight ? 'Switch to dark mode' : 'Switch to light mode'
      );

      // Save preference
      localStorage.setItem('theme', isLight ? 'light' : 'dark');
      console.log('Theme changed to:', isLight ? 'light' : 'dark');
    });

    // Keyboard support
    toggleButton.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleButton.click();
      }
    });
  }

  // Try multiple methods to ensure the button is created
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createToggleButton);
  } else {
    // DOM already loaded
    createToggleButton();
  }

  // Fallback - also try after window load
  window.addEventListener('load', createToggleButton);
})();
