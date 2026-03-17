# Nerdy 404 Page Skill

A complete design system for creating engineering-themed 404 error pages with AI lab anomaly aesthetics.

## Files

- `SKILL.md` - Complete design documentation and guidelines
- `template.html` - Full Hugo template implementation
- `README.md` - This file

## Quick Start

### For Hugo Sites

1. Copy `template.html` to `/layouts/404.html`
2. Update navigation URLs to match your site structure
3. Customize colors if needed (optional)
4. Test by visiting any non-existent URL

### For Other Static Site Generators

1. Consult your framework's 404 documentation
2. Adapt the template structure (remove Hugo template syntax)
3. Keep all CSS and JavaScript inline for portability

## Features

✅ AI lab anomaly + space ops theme
✅ Animated grid background
✅ Floating particles (13 total)
✅ Terminal-style error log with typing animation
✅ Glitch effect on 404 number
✅ Command-style navigation buttons
✅ Console easter eggs
✅ Fully responsive
✅ Zero external dependencies
✅ GPU-accelerated animations

## Customization

### Change Colors

Edit the color values in the CSS:
- Primary: `#8b5cf6` (purple)
- Error: `#ef4444` (red)
- Warning: `#f59e0b` (amber)
- Success: `#10b981` (green)
- Info: `#60a5fa` (blue)

### Change Copy

Update these sections in the HTML:
- `.status-chip` - Status badge text
- `.error-headline` - Main headline
- `.error-description` - Subheadline
- `.terminal-line` - Log messages
- Footer status text

### Change Navigation

Update the `.cmd-btn` links:
```html
<a href="YOUR_URL" class="cmd-btn">
  <span>ICON</span> command --text
</a>
```

## Theme Variants

See `SKILL.md` for three alternative themes:
1. Retro Terminal (green CRT)
2. Space Ops Dashboard (blue orbital)
3. AI Lab Anomaly (purple neural) ← Current

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari 14+, Chrome Mobile)

## Performance

- First paint: <100ms
- Page weight: ~15KB (inline, minified)
- Animations: 60fps (GPU accelerated)
- No external requests

## Testing Checklist

- [ ] Terminal lines animate sequentially
- [ ] Cursor blinks at 1s intervals
- [ ] Particles drift continuously
- [ ] Buttons glow on hover
- [ ] Mobile: buttons stack vertically
- [ ] All navigation links work
- [ ] Console messages appear in DevTools

## License

Free to use and modify for any project.

## Credits

Created: 2026-03-16
Design: AI lab anomaly + space ops polish
Brand fit: AI/ML/Data engineering audiences
