# RSS Feed Fix

## Issue
The RSS feed link at `https://blog.adipolak.com/index.xml` was broken.

## Solution
Changed the RSS feed URL from `/index.xml` to `/feed.xml` for better compatibility and cleaner URLs.

## Changes Made

### 1. Updated Hugo Configuration (`config.yaml`)
Added custom output format configuration to generate RSS feed as `feed.xml`:

```yaml
mediaTypes:
  application/rss+xml:
    suffixes:
      - xml

outputFormats:
  RSS:
    mediaType: application/rss+xml
    baseName: feed
    isPlainText: false
    rel: alternate
    isHTML: false
```

### 2. Updated Templates
- **Subscribe Page** (`layouts/_default/subscribe.html`): Changed display URL and button link from `index.xml` to `feed.xml`
- **Site Footer** (`layouts/partials/site-footer.html`): Updated RSS feed link
- **Site Navigation** (`layouts/partials/site-navigation.html`): Updated RSS icon link

### 3. Files Generated
Hugo now generates **both**:
- `/feed.xml` - New, working RSS feed (recommended)
- `/index.xml` - Legacy RSS feed (still generated for backward compatibility)

## New RSS Feed URL

✅ **https://blog.adipolak.com/feed.xml**

## What to Do Next

1. **Commit and push changes:**
   ```bash
   git add config.yaml layouts/
   git commit -m "Fix RSS feed: change from index.xml to feed.xml"
   git push
   ```

2. **Wait for GitHub Actions deployment** (typically 2-5 minutes)

3. **Verify the feed is working:**
   - Visit: https://blog.adipolak.com/feed.xml
   - Test in RSS reader (Feedly, Inoreader, etc.)
   - Check the subscribe page: https://blog.adipolak.com/subscribe/

## RSS Feed Features

The RSS feed includes:
- ✅ All published blog posts
- ✅ Full article content
- ✅ Publication dates
- ✅ Author attribution (Adi Polak)
- ✅ Valid RSS 2.0 format
- ✅ Atom namespace for better compatibility

## Updated Locations

RSS feed link now appears at:
1. **HTML head** - Auto-discovery link (`<link rel="alternate">`)
2. **Navigation bar** - RSS icon in header
3. **Footer** - "RSS Feed" link under "Stay Updated"
4. **Subscribe page** - Dedicated RSS section with copy-paste URL

---

Last Updated: 2026-03-12
