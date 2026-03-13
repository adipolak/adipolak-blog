# Presentations Sync Setup

This guide explains how to automatically sync your speaking engagements from Google Sheets or GitHub to your website.

## Option 1: Google Sheets (Recommended)

### Step 1: Create Your Spreadsheet

1. Create a new Google Sheet with these columns (exact names):
   - `title` - Talk title
   - `event` - Conference/event name
   - `date` - Date in YYYY-MM-DD format
   - `location` - City or "Virtual"
   - `description` - Brief description
   - `slides_url` - Link to slides (optional)
   - `video_url` - Link to recording (optional)
   - `thumbnail` - Image URL (optional)
   - `status` - Either "upcoming" or "past"

### Step 2: Publish as CSV

1. In Google Sheets, go to **File → Share → Publish to web**
2. Choose the sheet with your presentations
3. Select **Comma-separated values (.csv)** as the format
4. Click **Publish**
5. Copy the published CSV URL (looks like: `https://docs.google.com/spreadsheets/d/e/.../pub?output=csv`)

### Step 3: Set Up Automatic Sync

#### Method A: GitHub Actions (Fully Automated)

1. Create `.github/workflows/sync-presentations.yml`:

```yaml
name: Sync Presentations

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:  # Manual trigger
  push:
    branches: [main]

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install pyyaml requests

      - name: Sync presentations
        env:
          SHEETS_URL: ${{ secrets.PRESENTATIONS_SHEET_URL }}
        run: python scripts/sync-presentations.py

      - name: Commit changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add data/presentations.yaml
          git diff --quiet && git diff --staged --quiet || git commit -m "Update presentations from Google Sheets"
          git push
```

2. Add your Google Sheets CSV URL as a GitHub secret:
   - Go to your repo → **Settings → Secrets and variables → Actions**
   - Click **New repository secret**
   - Name: `PRESENTATIONS_SHEET_URL`
   - Value: Your Google Sheets CSV URL

3. The script already exists at `scripts/sync-presentations.py`

#### Method B: Manual Sync (Run Locally)

1. Set environment variable with your sheet URL:
   ```bash
   export SHEETS_URL="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv"
   ```

2. Run the sync script:
   ```bash
   python scripts/sync-presentations.py
   ```

3. Commit and push:
   ```bash
   git add data/presentations.yaml
   git commit -m "Update presentations"
   git push
   ```

---

## Option 2: GitHub Repository

Store presentations in a separate GitHub repository and sync them.

### Step 1: Create Presentations Repository

Create a repo with a `presentations.yaml` file:

```yaml
presentations:
  - title: "Your Talk Title"
    event: "Conference Name"
    date: "2026-06-15"
    location: "San Francisco, CA"
    description: "Talk description"
    slides_url: ""
    video_url: ""
    thumbnail: ""
    status: "upcoming"
```

### Step 2: Set Up GitHub Action

Create `.github/workflows/sync-presentations-repo.yml`:

```yaml
name: Sync Presentations from Repo

on:
  schedule:
    - cron: '0 */6 * * *'
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Download presentations
        run: |
          curl -o data/presentations.yaml \
            https://raw.githubusercontent.com/YOUR-USERNAME/presentations/main/presentations.yaml

      - name: Commit changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add data/presentations.yaml
          git diff --quiet && git diff --staged --quiet || git commit -m "Sync presentations"
          git push
```

---

## Option 3: Manual Update

Simply edit `data/presentations.yaml` directly:

```yaml
presentations:
  - title: "My Upcoming Talk"
    event: "KubeCon 2026"
    date: "2026-09-20"
    location: "Amsterdam"
    description: "Deep dive into Kubernetes operators"
    slides_url: ""
    video_url: ""
    status: "upcoming"  # Shows on homepage as "Upcoming Talk"

  - title: "Past Talk"
    event: "Data Summit 2025"
    date: "2025-11-15"
    location: "Virtual"
    description: "ML pipelines at scale"
    slides_url: "https://slides.com/yourslides"
    video_url: "https://youtube.com/watch?v=..."
    status: "past"  # Shows on /presentations/ page only
```

---

## How It Works

### Homepage Display

- Only **upcoming talks** (status: "upcoming") appear on the homepage
- The most recent upcoming talk is featured
- Past talks don't show on the homepage

### Presentations Page

- Shows all talks grouped by year
- Both upcoming and past talks appear
- Links to slides/videos when available

### Status Field

- `status: "upcoming"` - Shows on homepage + presentations page
- `status: "past"` - Shows on presentations page only

---

## Testing Your Setup

1. Add a test talk with status "upcoming"
2. Run: `hugo server`
3. Visit `http://localhost:1313/`
4. Check if your talk appears in the "Featured Content" section
5. Visit `/presentations/` to see all talks

---

## Troubleshooting

**Talk not showing on homepage?**
- Check that `status: "upcoming"` is set
- Verify the date is in the future
- Make sure YAML syntax is correct (proper indentation)

**Google Sheets sync not working?**
- Verify the sheet is published to web as CSV
- Check the CSV URL is correct and accessible
- Review GitHub Actions logs for errors

**Need help?**
- Check Hugo build logs: `hugo --verbose`
- Validate YAML: Use [yamllint.com](http://www.yamllint.com/)
