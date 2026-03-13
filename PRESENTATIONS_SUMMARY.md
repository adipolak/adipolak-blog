# Presentations Page - Google Sheets Integration ✅

## What Was Created

A complete **speaking/presentations page system** that can be automatically updated from a Google Spreadsheet, inspired by https://speaking.gamov.io/

## 🎨 Design Features

### Editorial & Warm
- Matches your blog's warm, sophisticated aesthetic
- Clean typography and hierarchy
- Comfortable spacing
- Professional but approachable

### Two Layouts

**1. Featured Talks** (top of page)
- Large cards with thumbnails
- Full descriptions
- Event name, date, location
- Links to slides and videos
- Gradient placeholders if no image

**2. Timeline View** (chronological)
- Grouped by year
- Compact format for scanning
- Quick access to resources
- Organized newest to oldest

## 📊 Google Sheets Integration

### How It Works

1. **Create a Google Sheet** with your talks
2. **Publish to web** as CSV
3. **Add URL to GitHub Secrets**
4. **Auto-syncs daily** (or on-demand)

### Spreadsheet Columns

| Column | Required | Description |
|--------|----------|-------------|
| title | ✅ | Talk title |
| event | ✅ | Conference/event name |
| date | ✅ | YYYY-MM-DD format |
| location | | City or "Virtual" |
| description | | 1-2 sentences (shows on featured talks) |
| slides_url | | Link to slides |
| video_url | | Link to video |
| thumbnail | | 16:9 image URL |
| featured | | TRUE/FALSE (marks as featured) |

## 🚀 Files Created

```
✅ layouts/_default/presentations.html    - Page template
✅ content/presentations-page.md          - Page content
✅ data/presentations.yaml                - Data file
✅ scripts/sync-presentations.py          - Sync script
✅ .github/workflows/sync-presentations.yml - Auto-sync workflow
✅ PRESENTATIONS_SETUP.md                 - Complete setup guide
```

## 📝 Two Ways to Update

### Option 1: Google Sheets (Recommended)
- Edit spreadsheet anytime
- Auto-syncs daily at 6 AM UTC
- Manual trigger via GitHub Actions
- See `PRESENTATIONS_SETUP.md` for setup

### Option 2: Manual Edit
- Edit `data/presentations.yaml` directly
- Commit and push changes
- Rebuilds automatically

## 🎯 What Shows Where

### Homepage `/`
- Speaking section teaser
- Link to full presentations page

### Presentations Page `/presentations/`
- Featured talks with full details
- Complete chronological timeline
- All links and resources

### Navigation
- Updated menu with "presentations" link
- Added "writing" link for blog posts

## ⚡ Features

**Automatic Updates**
- Daily sync from Google Sheets
- No manual rebuilding needed
- Updates push to GitHub

**Flexible Content**
- Mark best talks as "featured"
- Include descriptions for featured talks
- Optional slides/video links
- Optional thumbnails

**SEO Friendly**
- Structured data
- Clean URLs
- Mobile responsive

**Professional Design**
- Matches editorial aesthetic
- Warm, credible presentation
- Easy to scan and browse

## 🔧 Quick Start

### For Now (Manual)

Edit `data/presentations.yaml`:

```yaml
presentations:
  - title: "Your Talk Title"
    event: "Conference Name"
    date: "2024-03-15"
    location: "San Francisco"
    description: "What this talk was about"
    slides_url: "https://..."
    video_url: "https://..."
    featured: true
```

### For Later (Auto-Sync)

1. Create Google Sheet
2. Add your talks
3. Follow `PRESENTATIONS_SETUP.md`
4. Set and forget!

## 💡 Pro Tips

**For Credibility:**
- List well-known conferences
- Include video links when possible
- Show variety in topics
- Keep descriptions concise

**For Featured Talks:**
- Choose your 2-3 best talks
- Write compelling descriptions
- Include quality thumbnails
- Link to slides and video

**For Timeline:**
- Keep it chronological
- Include all talks (even small ones)
- Add location for context

## 🎨 Design Highlights

- **Warm neutral colors** - Not cold tech vibes
- **Editorial typography** - Serif headings, clean sans body
- **Generous spacing** - Room to breathe
- **Subtle interactions** - Hover states, smooth transitions
- **Gradient placeholders** - Beautiful even without images

## 📱 Responsive

- Desktop: Side-by-side for featured talks
- Tablet: Optimized grid
- Mobile: Stacked, touch-friendly

## 🌟 Why This Works

Like Viktor Gamov's page (speaking.gamov.io), this system:
- ✅ Shows your speaking credibility
- ✅ Provides easy access to resources
- ✅ Can be updated from anywhere
- ✅ Looks professional and polished
- ✅ Matches your personal brand

But better because:
- 🎨 Warmer, more approachable design
- 📊 Auto-updates from spreadsheet
- 🎯 Featured talks highlight best work
- 💅 Matches your blog's editorial aesthetic

## 📖 Next Steps

1. **View the page**: http://localhost:1313/presentations/
2. **Add your talks** to `data/presentations.yaml`
3. **(Optional) Set up Google Sheets** sync later
4. **Push to production** when ready

Your presentations page is ready to showcase your thought leadership! 🎤

See `PRESENTATIONS_SETUP.md` for complete Google Sheets integration instructions.
