# External Writing Section Guide

Your website now has a "Writing Across the Web" section to showcase articles you've published on other platforms!

## 📍 Where to Find It

**URL**: https://blog.adipolak.com/external-writing/

**Navigation**: The section appears in your main menu as "published elsewhere" with an external link icon.

## 📝 How to Add Your Articles

Edit the file: `data/external-writing.yaml`

### Article Format

```yaml
- title: "Your Article Title"
  publication: "Publication Name (e.g., InfoQ, The New Stack, DZone)"
  date: "YYYY-MM-DD"
  url: "https://full-article-url.com"
  description: "Brief 1-2 sentence description of what the article covers"
  tags: ["tag1", "tag2", "tag3"]
```

### Example

```yaml
- title: "Building Real-Time AI Systems with Kafka and Flink"
  publication: "InfoQ"
  date: "2025-11-15"
  url: "https://www.infoq.com/articles/real-time-ai-kafka-flink/"
  description: "Deep dive into architecting real-time AI systems using Apache Kafka and Flink for production-grade streaming applications."
  tags: ["AI", "Kafka", "Flink", "Real-time"]
```

## 🎨 Design Features

The section matches your site's warm editorial aesthetic:

- **Clean cards**: Each article displayed in an elegant card layout
- **Publication badges**: Publication name prominently displayed at the top
- **External link indicators**: Small arrow icon showing the link goes to another site
- **Responsive grid**: Automatically adjusts from 1 to 3 columns based on screen size
- **Tags**: Up to 4 tags displayed per article for easy topic identification
- **Dates**: Formatted consistently with the rest of your site

## 🔄 Keeping It Updated

**Manual Updates:**
1. Edit `data/external-writing.yaml`
2. Add new articles at the top (most recent first)
3. Rebuild your site with `hugo`

**Google Sheets Sync (Optional):**
You can create a sync script similar to your presentations sync:
- Create a Google Sheet with columns: title, publication, date, url, description, tags
- Adapt `scripts/sync-presentations.py` to work with external-writing.yaml
- Run automatically via cron job or GitHub Actions

## 📊 What Publications to Include

Consider adding articles from:
- Tech publications (InfoQ, The New Stack, DZone, DEV.to)
- Industry magazines
- Company engineering blogs (Confluent, Databricks, etc.)
- Conference proceedings/write-ups
- Guest posts on popular blogs
- Academic or research publications
- Medium or Substack cross-posts

## 🎯 SEO & Attribution Benefits

Each external article:
- ✅ Links back to the original publication (good for relationships)
- ✅ Shows breadth of your expertise across platforms
- ✅ Increases your site's authority by association
- ✅ Provides more entry points for AI systems to understand your work
- ✅ Helps visitors discover your full body of work in one place

## 🖼️ Optional: Add Publication Logos

You can enhance the cards by adding publication logos:

1. Add a `logo` field to each article:
   ```yaml
   - title: "..."
     publication: "InfoQ"
     logo: "/images/publications/infoq-logo.png"
     # ... rest of fields
   ```

2. Save publication logos in `static/images/publications/`

3. The template will automatically display them if present

## 📱 Mobile Responsive

The grid automatically adjusts:
- **Desktop**: 3 columns
- **Tablet**: 2 columns
- **Mobile**: 1 column

All cards remain fully readable and clickable at any screen size.

## 🔗 Integration with Rest of Site

The section includes:
- **Warm editorial header**: Matches homepage hero style
- **CTA section**: Encourages visitors to check your blog and subscribe
- **Consistent navigation**: Fits seamlessly into your site menu
- **Color scheme**: Uses your site's warm palette (peachy links, dark backgrounds)

## ✨ Current Status

The section is **live and ready to use**!

Currently showing 3 example articles. Replace these with your actual publications by editing `data/external-writing.yaml`.

---

## Quick Start Checklist

- [ ] Open `data/external-writing.yaml`
- [ ] Replace example articles with your real publications
- [ ] Add at least 3-5 articles to start
- [ ] Check the page at `/external-writing/` locally
- [ ] Deploy to see it live!

---

Last Updated: 2026-03-12
