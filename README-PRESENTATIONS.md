# Presentations Setup - Quick Start

Your website now shows **upcoming talks** on the homepage and all talks on `/presentations/`.

## 🎯 What You Need to Do

Replace the example talks in `data/presentations.yaml` with your real talks.

## 3 Ways to Manage Your Talks

### Option 1: Google Sheets (Easiest for Frequent Updates)

**Best for:** Regular speakers who update talks often

1. Create a Google Sheet with your talks
2. Publish it as CSV
3. Set up auto-sync

📖 **Full guide:** See `PRESENTATIONS-SYNC.md`
📋 **Template:** See `GOOGLE-SHEETS-TEMPLATE.md`

### Option 2: Edit YAML File Directly (Simplest)

**Best for:** Occasional updates

Edit `data/presentations.yaml`:

```yaml
presentations:
  - title: "Your Talk Title"
    event: "Conference Name"
    date: "2026-06-15"
    location: "San Francisco, CA"
    description: "What your talk is about"
    status: "upcoming"  # or "past"
```

### Option 3: Separate GitHub Repo (Advanced)

**Best for:** Sharing talks across multiple sites

Store talks in a separate repo and auto-sync.

📖 **Full guide:** See `PRESENTATIONS-SYNC.md`

## How It Works

### Homepage
- Shows **only upcoming talks** (status: "upcoming")
- Displays the next upcoming talk as "Featured"
- Perfect for promoting what's next

### /presentations/ Page
- Shows **all talks** (upcoming + past)
- Grouped by year
- Links to slides/videos when available

## Quick Edit Example

Replace the example data in `data/presentations.yaml`:

```yaml
presentations:
  - title: "Building Real-time ML Pipelines"
    event: "MLOps World 2026"
    date: "2026-08-20"
    location: "Austin, TX"
    description: "How we built ML pipelines that process millions of events per second"
    slides_url: ""
    video_url: ""
    status: "upcoming"

  - title: "Delta Lake in Production"
    event: "Data+AI Summit 2025"
    date: "2025-11-15"
    location: "San Francisco, CA"
    description: "Lessons from running Delta Lake at scale"
    slides_url: "https://speakerdeck.com/yourslides"
    video_url: "https://youtube.com/watch?v=..."
    status: "past"
```

## Testing

```bash
# Build and preview
hugo server

# Check homepage
open http://localhost:1313/

# Check presentations page
open http://localhost:1313/presentations/
```

## Questions?

- **Where are presentations stored?** `data/presentations.yaml`
- **How do I add slides/video later?** Just update the `slides_url` or `video_url` fields
- **Can I have multiple upcoming talks?** Yes! The homepage shows the most recent upcoming talk
- **What if I don't want to show any talk on homepage?** Set all talks to `status: "past"`

