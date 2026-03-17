---
name: add-presentation
description: Add a new talk or presentation to the presentations archive with all metadata. Use when adding conference talks, keynotes, workshops, or speaking engagements.
disable-model-invocation: false
allowed-tools: Read, Edit, Bash
---

# Add Presentation to Archive

Add a new talk or presentation to the archive at `data/presentations.yaml`.

## Required Information

When invoked, prompt the user for:

1. **Title** - The full talk title (e.g., "Beyond Prompting: Context Engineering at Scale")
2. **Event** - Conference/event name (e.g., "QCon AI New York")
3. **Date** - Talk date in YYYY-MM-DD format
4. **Location** - City, Country or State (e.g., "New York, NY" or "Virtual")

## Optional Information

5. **Description** - 1-2 sentence summary of the talk content and key themes
6. **Slides URL** - Link to slide deck (SlideShare, Speaker Deck, conference site, etc.)
7. **Video URL** - Link to recording (YouTube, Vimeo, conference portal, etc.)
8. **Thumbnail** - Image path relative to static folder (e.g., "/images/qcon-ai.jpg")

## Instructions

### 1. Read Current Data

Read `data/presentations.yaml` to understand the structure and existing entries.

### 2. Determine Status

Automatically set status based on date:
- If date is in the past: `status: "past"`
- If date is in the future: `status: "upcoming"`

### 3. Determine Correct Placement

Presentations are organized chronologically:
- Group by year (with `# YYYY` comment headers)
- Within each year, sort newest first (descending date order)
- If adding to a new year, create a new year section with comment header

### 4. Format the Entry

Follow this exact structure:

```yaml
  - title: "Talk Title Here"
    event: "Event Name"
    date: "YYYY-MM-DD"
    location: "City, State/Country"
    description: "Brief 1-2 sentence description."
    slides_url: "https://..."
    video_url: "https://..."
    thumbnail: "/images/filename.jpg"
    status: "past"
```

**Important YAML formatting rules:**
- Use 2-space indentation for the list item (`- title:`)
- Use 4-space indentation for all other fields
- Leave empty strings for missing optional fields: `slides_url: ""`
- Always include blank line between entries
- Maintain year comment headers: `# YYYY`

### 5. Insert the Entry

Use the Edit tool to add the entry:
- Find the correct year section (or create one)
- Insert in chronological position within that year
- Ensure proper indentation and blank lines
- Preserve existing formatting

### 6. Validate

Run `hugo --quiet` to verify:
- YAML syntax is valid
- Hugo builds successfully
- If build fails, fix YAML errors and retry

## Example Interaction

**User provides:**
```
Title: Building Real-Time AI with Kafka
Event: Data Summit 2026
Date: 2026-04-15
Location: San Francisco, CA
Description: Deep dive into real-time AI systems using Kafka and Flink for context management
Slides: https://speakerdeck.com/adipolak/real-time-ai
Video: (leave empty)
Thumbnail: (leave empty)
```

**You add:**
```yaml
# 2026
  - title: "Building Real-Time AI with Kafka"
    event: "Data Summit 2026"
    date: "2026-04-15"
    location: "San Francisco, CA"
    description: "Deep dive into real-time AI systems using Kafka and Flink for context management"
    slides_url: "https://speakerdeck.com/adipolak/real-time-ai"
    video_url: ""
    thumbnail: ""
    status: "upcoming"
```

## Common Event Types

Based on existing presentations:
- **Major Conferences**: QCon, KubeCon, Data & AI Summit, Microsoft Build, Devoxx
- **Regional Events**: Kafka Tel Aviv, DSWT Tel Aviv, AgentCon
- **Online**: O'Reilly Superstream, Confluent Meetups
- **Corporate**: DBX DevConnect, Bloomberg Intelligence Day
- **Meetups**: Local user groups and developer communities

## Common Topics/Keywords

For description writing, common themes include:
- **AI/ML**: Agentic AI, AI agents, RAG, context engineering, production AI
- **Streaming**: Kafka, Flink, real-time processing, data streaming
- **Architecture**: Distributed systems, data architecture, shift-left, stream-native
- **DevOps**: Kubernetes, cloud-native, infrastructure

## URL Patterns

Common slide/video hosting platforms:
- **Slides**: Speaker Deck, SlideShare, conference sites (qconferences.com, etc.)
- **Videos**: YouTube, Vimeo, InfoQ, conference portals
- **Conference pages**: Often have both slides and video links

## Special Cases

### Upcoming Talks
- Set `status: "upcoming"`
- Usually slides_url and video_url are empty
- Can update later when resources become available

### Workshop vs Talk
- Workshops often have longer descriptions
- May include "Hands-on workshop" in title or description

### Keynotes
- Often from major conferences
- May note "Track host" or "Keynote" in description

### Panel Discussions
- May have multiple speakers
- Description should clarify format if relevant

## Success Criteria

✅ YAML is syntactically valid (Hugo builds without errors)
✅ Entry is in correct chronological position
✅ All required fields are present
✅ Status is correctly set (past/upcoming)
✅ Optional fields use empty strings ("") if not provided
✅ Proper indentation (2 spaces for list, 4 for fields)
✅ Year comment header exists for the entry's year
✅ Blank line between entries for readability

## Error Handling

If Hugo build fails:
1. Check YAML indentation (must be exact)
2. Verify quotes are balanced in all string values
3. Ensure date format is YYYY-MM-DD
4. Check for special characters that need escaping
5. Fix and re-run Hugo build until successful
