---
name: add-external-writing
description: Add a new article to the external writing list with all metadata and optional featured image. Use when publishing articles on external platforms.
disable-model-invocation: false
allowed-tools: Read, Edit, Bash, WebFetch
---

# Add External Writing Article

Add a new article to the external writing collection at `data/external_writing.yaml`.

## Required Information

When invoked, prompt the user for:
1. **Title** - The full article title (as published)
2. **Publication** - Where it was published (e.g., "VentureBeat", "InfoWorld", "Forbes Tech Council")
3. **Date** - Publication date in YYYY-MM-DD format
4. **URL** - The full article URL
5. **Tags** - Array of relevant tags (e.g., ["ai", "leadership", "enterprise ai"])
6. **Image** (optional) - Featured image URL from the article

## Instructions

1. **Read the current external_writing.yaml file** to understand the structure and existing entries

2. **Determine the correct placement** based on the date:
   - Articles are organized by year (with `# YYYY` comment headers)
   - Within each year, articles are sorted newest first (descending date order)
   - If adding an article from a new year, create a new year section

3. **Generate a description** (1-2 sentences):
   - If a URL is provided and WebFetch is available, try to fetch the article to extract key points
   - If WebFetch fails or is unavailable, create a concise description based on the title and tags
   - Focus on the article's main value proposition and key insights
   - Keep it professional and informative

4. **Format the new entry** following this structure:
   ```yaml
   - title: "Article Title"
     publication: "Publication Name"
     date: "YYYY-MM-DD"
     url: "https://..."
     image: "https://..." # optional, only include if provided
     description: "Brief 1-2 sentence description of the article's main points."
     tags: ["tag1", "tag2", "tag3"]
   ```

5. **Insert the entry** in the correct chronological position:
   - Use the Edit tool to add the entry
   - Ensure proper YAML indentation (2 spaces)
   - Maintain blank lines between entries for readability

6. **Verify the update**:
   - Run `hugo --quiet` to ensure the YAML is valid and Hugo builds successfully
   - If build fails, fix any YAML syntax errors

## Tips for Images

- Featured images should be direct image URLs (PNG, JPG, etc.)
- Images display at 200px height with hover zoom effect
- Common patterns:
  - VentureBeat: `https://venturebeat.com/_next/image?url=...`
  - InfoWorld: `https://www.infoworld.com/wp-content/uploads/...`
  - Forbes: `https://imageio.forbes.com/specials-images/...`
  - InfoQ: `https://imgopt.infoq.com/fit-in/...`
  - Confluent: `https://images.ctfassets.net/...`

## Common Tag Suggestions

Based on existing articles, commonly used tags include:
- AI/ML: "ai", "machine-learning", "agentic ai", "rag", "ai agents"
- Data Engineering: "kafka", "flink", "iceberg", "stream processing", "data engineering"
- Systems: "distributed-systems", "data architecture", "data fabric"
- Leadership: "leadership", "enterprise ai", "business value"
- Developer: "developer tools", "devex", "software development"
- Events: "qcon", "conference"

## Success Criteria

- YAML is syntactically valid
- Entry is in correct chronological position
- Hugo builds without errors
- All required fields are present
- Description is informative and concise
