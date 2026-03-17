---
name: create-404-page
description: Create a nerdy, engineering-themed 404 error page with AI lab anomaly aesthetics. Use for Hugo sites or static site generators.
disable-model-invocation: false
allowed-tools: Read, Write, Edit, Bash
---

# Nerdy 404 Page Design System

Create an engineering-focused 404 page with "AI lab anomaly + space ops polish" aesthetics.

## Design Philosophy

Target audience: Technical professionals, developers, AI/data engineers
Tone: Clever, self-aware, not too serious, shows personality without being unprofessional
Theme: AI/ML system error mixed with space operations dashboard

## Core Visual Elements

### Color Palette
- **Background**: Dark gradients (#0a0a0f to #11100f)
- **Accent colors**:
  - Purple (#8b5cf6, #7c3aed) - primary interactive elements
  - Pink/Magenta (#ec4899) - gradient accents
  - Amber (#f59e0b) - warnings, terminal dots
  - Red (#ef4444) - errors, status alerts
  - Green (#10b981) - terminal text, success states
  - Blue (#60a5fa) - info messages

### Typography
- **Monospace**: 'Monaco', 'Menlo', 'Courier New' - for terminal, code, commands
- **Sans-serif**: System fonts (-apple-system, BlinkMacSystemFont, "Segoe UI") - for headlines
- **404 Number**: 4-8rem, bold, gradient text with glow/blur shadow

### Animations
1. **Grid background**: Pulsing opacity (30-50%) on 4s loop
2. **Floating particles**: 13+ particles drifting upward at varied speeds (15-25s)
3. **Glitch effect**: Subtle position shift on 404 number every ~3s
4. **Terminal typing**: Sequential fade-in of terminal lines with staggered delays
5. **Cursor blink**: Standard terminal cursor at 1s intervals
6. **Status chip**: Opacity pulse for "ANOMALY DETECTED" badge
7. **Button hovers**: Lift (-2px translateY) + glow shadow

## Content Strategy

### Headline Copy (Pick theme-appropriate)
- "This page drifted outside the context window."
- "Page embedding returned NULL"
- "Route not found in vector space"
- "Undefined behavior detected"
- "This endpoint does not exist in this universe"

### Subheadline
- "We tried retrieval, ranking, and a light amount of panic. No match found."
- "Attempted: semantic search, brute force, asking nicely. Status: 404."

### Terminal Log Messages
Use color-coded log lines that tell a story:
- INFO (green/blue): "initializing page retrieval...", "querying knowledge graph..."
- WARNING (amber): "warning: route not found in index"
- ERROR (red): "ERROR: Page embedding returned NULL"
- CONTEXT (green): "possible causes: typo | moved route | cosmic bit flip"

### Footer Status Bar
Nerdy status updates showing system state:
- "Status: mildly panicking | AI systems operational | quantum state: uncertain"
- "Confidence: 0.004 | Tokens processed: 0 | Sanity check: failed"

## Terminal Card Design

```
┌─ [●●●] system.log ──────────────────┐
│ > initializing page retrieval...     │
│ > querying knowledge graph...        │
│ > warning: route not found in index  │
│ > checking backup vectors...         │
│ > ERROR: Page embedding returned NULL│
│ > possible causes: typo | moved...▊  │
└──────────────────────────────────────┘
```

**Requirements**:
- Header with 3 colored dots (red, amber, green) mimicking macOS window
- Monospace font throughout
- Color-coded messages (green normal, blue info, amber warning, red error)
- Blinking cursor at end
- Semi-transparent dark background with border
- Subtle backdrop blur effect

## Command-Style Navigation

Create buttons that look like terminal commands:

**Primary Action** (gradient purple background):
- `→ cd /home`

**Secondary Actions** (transparent with border):
- `📝 explore --writing`
- `🎤 list --talks`
- `🔍 grep --site`

**Button Specs**:
- Font: Monaco/Menlo monospace
- Size: 0.875rem
- Padding: 12px 24px
- Border: 1px solid with glow on hover
- Transition: all 0.3s ease
- Hover effect: Lift 2px + increase glow + brighten background

## Layout Structure

```
┌─────────────────────────────────┐
│  [Animated grid background]     │
│  [Floating particles]            │
│                                  │
│  [ANOMALY DETECTED] ← status chip│
│                                  │
│        404  ← glitch effect      │
│                                  │
│   This page drifted outside...   │
│   We tried retrieval...          │
│                                  │
│  ┌─────────────────────────┐    │
│  │ [Terminal card]          │    │
│  │ > log messages here...   │    │
│  └─────────────────────────┘    │
│                                  │
│  [→ cd /home] [explore] [grep]   │
│                                  │
│  Status: mildly panicking...     │
└─────────────────────────────────┘
```

## Technical Implementation

### Hugo Template Structure
```html
{{ define "main" }}
<style>
  /* Inline all CSS in the template */
</style>

<div class="error-404-container">
  <div class="grid-bg"></div>

  <!-- 5 static particles -->
  <div class="particle" style="..."></div>

  <div class="error-404-content">
    <div class="status-chip">ANOMALY DETECTED</div>
    <h1 class="error-code glitch">404</h1>
    <h2 class="error-headline">...</h2>
    <p class="error-description">...</p>

    <div class="terminal-card">
      <div class="terminal-header">
        <div class="terminal-dot"></div>
        <div class="terminal-dot"></div>
        <div class="terminal-dot"></div>
      </div>
      <div class="terminal-body">
        <div class="terminal-line">...</div>
      </div>
    </div>

    <div class="command-buttons">
      <a href="..." class="cmd-btn primary">...</a>
    </div>
  </div>
</div>

<script>
  // Add random particles dynamically
  // Optional console easter eggs
</script>
{{ end }}
```

### Key CSS Classes

**Container**: `.error-404-container`
- min-height: 80vh
- Dark gradient background
- position: relative (for absolute particle positioning)

**Grid**: `.grid-bg`
- Repeating linear gradient creating grid pattern
- Animated opacity pulse
- pointer-events: none

**Particles**: `.particle`
- 2px × 2px dots
- Purple glow
- Transform animation from bottom to top
- Random delays and durations

**Error code**: `.error-code`
- Gradient text effect
- ::after pseudo-element for glow shadow
- Glitch animation

**Terminal**: `.terminal-card`
- Semi-transparent dark background
- Border with purple glow
- Backdrop blur

### Performance Optimizations
- Use transform and opacity for animations (GPU accelerated)
- Inline critical CSS to avoid flash
- Limit particle count (8-13 total)
- Use will-change sparingly
- Minimal external dependencies (zero if possible)

### Responsive Design
```css
@media (max-width: 640px) {
  .error-code { font-size: 4rem; }
  .command-buttons { flex-direction: column; }
  .cmd-btn { width: 100%; }
}
```

## Easter Eggs

Add console messages for developers who open DevTools:
```javascript
console.log('%c404 Error Handler', 'color: #8b5cf6; font-size: 20px;');
console.log('%cPage quantum state: superposition...', 'color: #60a5fa;');
```

## Customization Options

### Three Theme Variants

1. **Retro Terminal** (Green CRT aesthetic)
   - Green (#10b981) primary color
   - Scanline effect overlay
   - ASCII art instead of particles

2. **Space Ops Dashboard** (Blue orbital theme)
   - Blue (#60a5fa) primary color
   - Radar/orbital animations
   - "Lost satellite" messaging

3. **AI Lab Anomaly** (Purple neural theme) ← **Recommended**
   - Purple (#8b5cf6) primary color
   - Neural network node background
   - "Outside context window" messaging

## Brand Alignment

For AI/ML/Data focused personal brands:
- Use "context window", "embedding", "vector", "retrieval" terminology
- Reference AI concepts playfully but accurately
- Maintains technical credibility while showing personality
- Demonstrates both technical depth and design sensibility

## Testing Checklist

- [ ] All animations render smoothly (60fps)
- [ ] Terminal lines appear sequentially
- [ ] Cursor blinks at correct speed
- [ ] Particles drift upward continuously
- [ ] Buttons have hover states with glow
- [ ] Mobile responsive (buttons stack)
- [ ] All navigation links work correctly
- [ ] Page loads in <500ms
- [ ] Accessible (keyboard navigation, aria labels)
- [ ] Console easter eggs appear

## File Location

For Hugo sites: `/layouts/404.html`
For other SSGs: Consult framework's 404 page documentation

## Example Usage

When implementing for a new site:
1. Copy the complete HTML structure
2. Update navigation URLs to match site structure
3. Adjust color scheme to match brand (keep high contrast)
4. Customize copy to match technical domain
5. Test on actual 404 routes
6. Verify all links point to real pages
