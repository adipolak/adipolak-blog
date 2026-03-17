# Add Presentation Skill

Streamlines adding new talks and presentations to the archive at `data/presentations.yaml`.

## Files

- `SKILL.md` - Complete skill documentation and workflow
- `README.md` - This file

## Quick Reference

### Required Fields
- Title
- Event
- Date (YYYY-MM-DD)
- Location

### Optional Fields
- Description
- Slides URL
- Video URL
- Thumbnail path

### What the Skill Does

1. Prompts for all presentation details
2. Auto-detects if talk is past or upcoming based on date
3. Finds correct chronological position in YAML
4. Formats entry with proper indentation
5. Validates YAML syntax with Hugo build
6. Handles year section creation automatically

### Example Usage

**In conversation:**
> "Add a new presentation"
> or
> "/add-presentation"

**The skill will prompt for:**
```
Title: Beyond Prompting: Context Engineering at Scale
Event: QCon AI New York
Date: 2025-12-16
Location: New York, NY
Description: Stream-native context engineering using Kafka and Flink...
Slides: https://ai.qconferences.com/presentation/...
Video: (leave empty if not available)
Thumbnail: (leave empty if no image)
```

**Result:**
Entry added to `presentations.yaml` in correct position, Hugo validated.

## Common Workflows

### Adding a Recent Talk
Provide full details including slides if available. Video often comes later.

### Adding an Upcoming Talk
Only need basic info. Status automatically set to "upcoming". Can update later.

### Bulk Adding Historical Talks
Can invoke skill multiple times. Best to add newest to oldest within a year.

### Updating Existing Talk
Use Edit tool directly to add video_url or slides_url when they become available.

## Data Structure

Presentations are organized:
- By year (descending: 2026 → 2015)
- Within year, by date (descending: newest first)
- Each entry maintains consistent field order
- Empty optional fields use `""`

## Tips

- **Dates**: Use YYYY-MM-DD format (e.g., 2026-03-16)
- **Descriptions**: 1-2 sentences, focus on key themes and value
- **URLs**: Full URLs including https://
- **Thumbnails**: Relative paths from static folder (/images/...)
- **Location**: Can be "Virtual" for online events

## Validation

Skill automatically runs `hugo --quiet` to verify YAML is valid and site builds correctly.

## Future Enhancements

Possible additions:
- Auto-fetch event details from URL
- Topic/tag categorization
- Speaking type (keynote, workshop, panel)
- Co-speakers tracking
- Related blog post linking
