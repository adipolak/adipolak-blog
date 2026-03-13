# Dark Mode Toggle - Debugging Guide

## Expected Behavior

You should see a **purple circular button** in the bottom-right corner of every page with a moon emoji (🌙).

## Files Involved

1. **JavaScript**: `/static/js/theme-toggle.js` - Creates the button
2. **CSS**: `/static/css/custom.css` - Styles the button and dark mode
3. **HTML**: Button is injected via JavaScript after page loads

## Quick Debug Steps

### Step 1: Check Browser Console

1. Open your browser's Developer Tools (F12 or Cmd+Option+I on Mac)
2. Go to the **Console** tab
3. Look for these messages:
   ```
   Dark mode script loaded
   Current theme: light (or dark)
   Creating dark mode toggle button
   Toggle button added to page
   ```

### Step 2: Check if Button Exists

In the browser console, type:
```javascript
document.querySelector('.dark-mode-toggle')
```

**If it returns an element**: The button exists but might not be visible due to CSS
**If it returns `null`**: The JavaScript isn't creating the button

### Step 3: Force Create Button

If button doesn't exist, try creating it manually in console:
```javascript
const btn = document.createElement('button');
btn.className = 'dark-mode-toggle';
btn.innerHTML = '🌙';
btn.style.cssText = 'position:fixed; bottom:2rem; right:2rem; width:56px; height:56px; border-radius:50%; background:#7d1fa5; border:none; color:white; font-size:1.5rem; cursor:pointer; z-index:9999;';
document.body.appendChild(btn);
btn.onclick = () => document.body.classList.toggle('dark-mode');
```

### Step 4: Check CSS Loading

In console:
```javascript
getComputedStyle(document.querySelector('.dark-mode-toggle'))
```

This will show all the applied styles.

## Common Issues

### Issue 1: JavaScript Not Loading
**Check**: Visit http://localhost:1313/js/theme-toggle.js
**Expected**: You should see the JavaScript code
**Fix**: If 404, the file isn't being copied to public/

### Issue 2: CSS Not Applying
**Check**: Visit http://localhost:1313/css/custom.css
**Expected**: You should see CSS with `.dark-mode-toggle` styles
**Fix**: If 404 or missing styles, rebuild with `hugo`

### Issue 3: Button Hidden Behind Elements
**Check**: In Elements tab, find `.dark-mode-toggle` and check z-index
**Expected**: z-index should be 1000 or higher
**Fix**: Add `z-index: 9999 !important;` to the CSS

### Issue 4: Script Running Before DOM Ready
**Check**: Look for errors in console like "Cannot read property 'appendChild'"
**Expected**: Script should wait for DOM
**Fix**: Already handled in the script with multiple event listeners

## Alternative Solution: HTML-Only Toggle

If JavaScript isn't working, we can add the button directly in the HTML template:

Add to `layouts/partials/site-footer.html` or create a new partial:

```html
<button class="dark-mode-toggle" onclick="toggleDarkMode()" aria-label="Toggle dark mode">
  <span id="theme-icon">🌙</span>
</button>

<script>
function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  const isDark = document.body.classList.contains('dark-mode');
  document.getElementById('theme-icon').textContent = isDark ? '☀️' : '🌙';
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Apply saved theme on load
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  document.body.classList.add('dark-mode');
  if (document.getElementById('theme-icon')) {
    document.getElementById('theme-icon').textContent = '☀️';
  }
}
</script>
```

## Testing the Dark Mode Itself

Even without the toggle button, you can test dark mode manually:

1. Open browser console
2. Type: `document.body.classList.add('dark-mode')`
3. The page should switch to dark theme

To switch back:
```javascript
document.body.classList.remove('dark-mode')
```

## What Should Change in Dark Mode

When dark mode is active:
- Background: Black (#18191a)
- Text: Light gray (#e4e6eb)
- Cards: Dark gray (#242526)
- Borders: Darker (#3a3b3c)

## Still Not Working?

Please share:
1. Screenshot of your browser console
2. Screenshot of the page (especially bottom-right corner)
3. Browser and version you're using
4. Any error messages

I can then create a more targeted fix!
