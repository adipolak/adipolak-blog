# External Writing Sync Setup

This guide shows you how to manage your external articles using Google Sheets and automatically sync them to your website.

## 📊 Google Sheets Setup

### Step 1: Create Your Google Sheet

Create a new Google Sheet with these **exact column names**:

| title | publication | date | url | description | tags |
|-------|-------------|------|-----|-------------|------|
| Article Title | Publication Name | 1/18/2023 | https://... | Brief description | tag1, tag2, tag3 |

**Column Details:**
- **title**: Full article title
- **publication**: Publication name (e.g., "Forbes Tech Council", "InfoQ", "InfoWorld")
- **date**: Publication date (format: MM/DD/YYYY or YYYY-MM-DD)
- **url**: Full URL to the article
- **description**: 1-2 sentence summary of the article
- **tags**: Comma-separated tags (e.g., "AI, Kafka, Streaming")

### Step 2: Make Sheet Publicly Readable

1. Click **Share** button (top right)
2. Click **Change to anyone with the link**
3. Set to **Viewer** access
4. Click **Done**

### Step 3: Get CSV Export URL

1. In your Google Sheet, click **File** → **Share** → **Publish to web**
2. In the dropdown, select your sheet name (e.g., "Sheet1")
3. Change "Web page" to **"Comma-separated values (.csv)"**
4. Click **Publish**
5. Copy the URL that appears (it should end with `output=csv`)

Alternative method:
```
https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv&gid=0
```

Replace `YOUR_SHEET_ID` with your actual sheet ID from the URL.

## 🔄 Running the Sync

### Option 1: Using Environment Variable

```bash
export SHEETS_URL="https://docs.google.com/spreadsheets/d/.../export?format=csv"
python3 scripts/sync-external-writing.py
```

### Option 2: One-Line Command

```bash
SHEETS_URL="https://docs.google.com/spreadsheets/d/.../export?format=csv" python3 scripts/sync-external-writing.py
```

### Option 3: Save URL to .env File

Create a file `.env` in your project root:

```bash
SHEETS_URL="https://docs.google.com/spreadsheets/d/.../export?format=csv"
```

Then run:
```bash
source .env
python3 scripts/sync-external-writing.py
```

## 📝 CSV File Alternative

If you prefer to manage articles in a CSV file instead of Google Sheets:

### Step 1: Create CSV File

Create: `data/external-writing.csv`

```csv
title,publication,date,url,description,tags
"Article Title","Publication Name","2023-01-18","https://example.com","Description here","tag1, tag2"
```

### Step 2: Convert CSV to YAML

You can use the sync script with a local CSV:

```bash
# Modify the script to read from local file instead of URL
python3 scripts/sync-external-writing.py --local data/external-writing.csv
```

Or manually update `data/external-writing.yaml` following the format:

```yaml
articles:
  - title: "Article Title"
    publication: "Publication Name"
    date: "2023-01-18"
    url: "https://example.com"
    description: "Description here"
    tags: ["tag1", "tag2"]
```

## 🤖 Automated Sync (Optional)

### Using GitHub Actions

Create `.github/workflows/sync-external-writing.yml`:

```yaml
name: Sync External Writing

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:  # Manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Sync external writing
        env:
          SHEETS_URL: ${{ secrets.EXTERNAL_WRITING_SHEETS_URL }}
        run: python3 scripts/sync-external-writing.py

      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add data/external-writing.yaml
          git diff --quiet && git diff --staged --quiet || git commit -m "Sync external writing from Google Sheets"
          git push
```

**Setup:**
1. Go to GitHub repo → Settings → Secrets and variables → Actions
2. Create new secret: `EXTERNAL_WRITING_SHEETS_URL`
3. Paste your Google Sheets CSV export URL

### Using Cron (Local/Server)

Add to your crontab:

```bash
# Sync external writing daily at 2 AM
0 2 * * * cd /path/to/adipolak-blog && SHEETS_URL="https://docs.google.com/.../export?format=csv" python3 scripts/sync-external-writing.py && git add data/external-writing.yaml && git commit -m "Sync external writing" && git push
```

## 📋 Example Google Sheet

Here's what your sheet should look like:

| title | publication | date | url | description | tags |
|-------|-------------|------|-----|-------------|------|
| Agentic AI: The Top Challenges | InfoWorld | 1/7/2025 | https://www.infoworld.com/article/... | Key obstacles enterprises face when deploying agentic AI systems | AI Agents, Enterprise AI |
| 3 Data Engineering Trends | InfoWorld | 11/25/2024 | https://www.infoworld.com/article/... | Emerging trends in Kafka, Flink, and Iceberg | Kafka, Flink, Iceberg |

## ✅ Verification

After syncing, check:

```bash
# View the generated YAML
cat data/external-writing.yaml

# Build and preview locally
hugo server
# Visit: http://localhost:1313/external-writing/
```

## 🔍 Troubleshooting

**Problem**: "Error: SHEETS_URL environment variable not set"
- **Solution**: Make sure you've set the environment variable before running the script

**Problem**: "403 Forbidden" when fetching CSV
- **Solution**: Make sure your Google Sheet is set to "Anyone with the link can view"

**Problem**: Articles not appearing on website
- **Solution**: Rebuild your site with `hugo` or `hugo server`

**Problem**: Date format issues
- **Solution**: Use MM/DD/YYYY format in Google Sheets, the script will convert to YYYY-MM-DD

## 📦 Dependencies

The sync script requires:
```bash
pip install requests
```

## 🎯 Workflow

1. **Add article to Google Sheet** (or CSV)
2. **Run sync script** (manual or automated)
3. **Rebuild Hugo site** (`hugo`)
4. **Deploy** (push to GitHub, Netlify will auto-deploy)

---

**Quick Start:**
1. Copy Google Sheets template (see example above)
2. Add your articles
3. Get CSV export URL
4. Run: `SHEETS_URL="..." python3 scripts/sync-external-writing.py`
5. Done!

---

Last Updated: 2026-03-12
