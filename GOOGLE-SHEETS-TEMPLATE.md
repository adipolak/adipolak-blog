# Google Sheets Template for Presentations

Use this exact format for your Google Sheet to sync presentations automatically.

## Column Headers (Row 1)

Copy these exact column names into your first row:

```
title | event | date | location | description | slides_url | video_url | thumbnail | status
```

## Example Rows

| title | event | date | location | description | slides_url | video_url | thumbnail | status |
|-------|-------|------|----------|-------------|------------|-----------|-----------|--------|
| Real-time Data Pipelines at Scale | KubeCon Europe 2026 | 2026-04-15 | Amsterdam | Building real-time data pipelines with Kubernetes and Apache Flink | https://slides.com/myslides | https://youtube.com/watch?v=... | https://example.com/thumb.jpg | upcoming |
| ML in Production: Lessons Learned | MLOps Summit | 2025-11-20 | Virtual | Practical lessons from deploying ML models in production | https://speakerdeck.com/... | https://youtube.com/watch?v=... |  | past |
| Apache Spark 3.5 Deep Dive | Data+AI Summit | 2026-06-10 | San Francisco | New features and performance improvements in Spark 3.5 |  |  |  | upcoming |

## Field Descriptions

### Required Fields

- **title**: Your talk title (required)
- **event**: Conference or event name (required)
- **date**: Date in YYYY-MM-DD format (required)
- **location**: City name or "Virtual" (required)
- **description**: Brief description of your talk (required)
- **status**: Either "upcoming" or "past" (required)
  - `upcoming` = Shows on homepage + presentations page
  - `past` = Shows on presentations page only

### Optional Fields

- **slides_url**: Link to your slides (leave empty if not available yet)
- **video_url**: Link to recording (leave empty if not available yet)
- **thumbnail**: Image URL for talk preview (leave empty to use default gradient)

## Important Notes

1. **Date Format**: Must be `YYYY-MM-DD` (e.g., 2026-04-15, not 04/15/2026)
2. **Status**: Use lowercase "upcoming" or "past"
3. **Empty Fields**: Leave empty cells blank, don't put "N/A" or dashes
4. **No Extra Columns**: Only use the columns listed above

## Publishing Your Sheet

1. **File → Share → Publish to web**
2. Select your presentations sheet
3. Choose **Comma-separated values (.csv)**
4. Click **Publish**
5. Copy the CSV URL (starts with `https://docs.google.com/spreadsheets/d/e/`)

## Testing Your Sheet

Before setting up auto-sync, test manually:

```bash
# Set your sheet URL
export SHEETS_URL="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv"

# Run sync
python scripts/sync-presentations.py

# Check the output
cat data/presentations.yaml
```

## Quick Template Link

**👉 [Copy this Google Sheets Template](https://docs.google.com/spreadsheets/d/YOUR-TEMPLATE-ID/copy)** _(create and share your own template)_

Or create manually with the columns above.
