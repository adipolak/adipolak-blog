## Speaking & Presentations Page - Google Sheets Integration

Your presentations page can be automatically updated from a Google Spreadsheet, similar to https://speaking.gamov.io/

## 📊 Setup Google Sheets

### Step 1: Create Your Spreadsheet

Create a Google Sheet with these columns:

| title | event | date | location | description | slides_url | video_url | thumbnail | featured |
|-------|-------|------|----------|-------------|------------|-----------|-----------|----------|
| Talk Title | Conference Name | 2024-03-15 | San Francisco | Brief description | https://... | https://... | https://... | TRUE |

**Column Details:**
- **title**: Talk title (required)
- **event**: Conference/event name (required)
- **date**: YYYY-MM-DD format (required)
- **location**: City or "Virtual" (optional)
- **description**: 1-2 sentences about the talk (optional, shows on featured talks)
- **slides_url**: Link to slides (optional)
- **video_url**: Link to video recording (optional)
- **thumbnail**: Link to thumbnail image (optional, otherwise shows gradient placeholder)
- **featured**: TRUE/FALSE - marks as featured talk with full description (optional)

### Step 2: Publish to Web

1. In your Google Sheet, go to **File → Share → Publish to web**
2. Choose **Entire Document** or specific sheet
3. Select **Comma-separated values (.csv)**
4. Click **Publish**
5. Copy the URL (it will look like: `https://docs.google.com/spreadsheets/d/e/2PACX-.../pub?output=csv`)

### Step 3: Set Up Auto-Sync (GitHub Actions)

1. Go to your GitHub repository settings
2. Navigate to **Settings → Secrets and variables → Actions**
3. Click **New repository secret**
4. Name: `PRESENTATIONS_SHEET_URL`
5. Value: Paste your published CSV URL
6. Click **Add secret**

### Step 4: Enable Workflow

The GitHub Action workflow is already created at `.github/workflows/sync-presentations.yml`

It will:
- Run daily at 6 AM UTC
- Can be triggered manually from GitHub Actions tab
- Automatically fetch your spreadsheet
- Update `data/presentations.yaml`
- Commit and push changes

**To trigger manually:**
1. Go to **Actions** tab in GitHub
2. Select **Sync Presentations** workflow
3. Click **Run workflow**

## 🎨 Design Features

Your presentations page includes:

### Featured Talks Section
- Large cards with thumbnails
- Full descriptions
- Event name and date
- Links to slides and videos
- Mark talks as featured with `featured: TRUE` in spreadsheet

### Timeline View
- Chronologically organized by year
- Compact format for browsing history
- Quick access to slides/videos

### Warm Editorial Design
- Matches your blog's aesthetic
- Clean typography
- Subtle gradients for placeholders
- Comfortable spacing

## 📝 Manual Updates (Alternative)

If you prefer not to use Google Sheets, edit `data/presentations.yaml` directly:

```yaml
presentations:
  - title: "Building ML Systems at Scale"
    event: "Data Engineering Summit"
    date: "2024-03-15"
    location: "San Francisco"
    description: "Practical patterns for production ML"
    slides_url: "https://..."
    video_url: "https://..."
    thumbnail: "https://..."
    featured: true
```

## 🖼️ Thumbnail Images

**Best Practices:**
- Use 16:9 aspect ratio (e.g., 1280x720px)
- Host on a CDN or GitHub
- Or use first slide from your deck
- Leave blank for automatic gradient placeholder

**Where to get thumbnails:**
- First slide of your presentation
- Event photos
- Screenshot from video
- Custom graphics

## 🔄 Update Frequency

The auto-sync runs:
- **Daily** at 6 AM UTC
- **On-demand** via GitHub Actions
- Updates typically take 1-2 minutes

## 📱 Mobile Responsive

The design automatically adapts:
- Desktop: Side-by-side layout for featured talks
- Mobile: Stacked layout
- Timeline view optimizes for small screens

## 🎯 What Shows Where

### Homepage `/`
- Speaking section with link to full page

### Presentations Page `/presentations/`
- **Featured talks** (marked with `featured: TRUE`)
  - Full cards with thumbnails
  - Complete descriptions
  - Prominent display

- **All presentations timeline**
  - Grouped by year
  - Compact chronological list
  - Quick scan of speaking history

## 🚀 Going Live

1. Add your talks to Google Sheets
2. Publish sheet and add URL to GitHub Secrets
3. Run the workflow manually first to test
4. Your presentations page updates automatically!

## 💡 Pro Tips

**For Conference Organizers:**
- Mark your best talks as `featured`
- Add descriptions to featured talks
- Include video links when available

**For SEO:**
- Use descriptive titles
- Include keywords in descriptions
- Link to conference websites

**For Credibility:**
- List conferences chronologically
- Include well-known events
- Show variety in topics/locations

## 🔧 Troubleshooting

**Workflow not running?**
- Check GitHub Actions tab for errors
- Verify `PRESENTATIONS_SHEET_URL` secret is set
- Ensure sheet is published to web

**Data not showing?**
- Check YAML syntax in `data/presentations.yaml`
- Verify date format is YYYY-MM-DD
- Look for Hugo build errors

**Images not loading?**
- Ensure URLs are publicly accessible
- Use HTTPS URLs
- Consider hosting on GitHub or CDN

## 📊 Example Google Sheet

[Create a copy of this template](https://docs.google.com/spreadsheets/d/YOUR_TEMPLATE_ID/copy)

Your speaking page is now ready to showcase your thought leadership! 🎤
