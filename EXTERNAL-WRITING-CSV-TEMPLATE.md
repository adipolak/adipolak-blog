# External Writing CSV Template

## Option 1: Google Sheets (Recommended)

Create a Google Sheet with these columns and data:

### Column Headers (Row 1)
```
title | publication | date | url | description | tags
```

### Example Data (Copy to Google Sheets)

```
title,publication,date,url,description,tags
"Agentic AI: The Top Challenges and How to Overcome Them","InfoWorld","1/7/2025","https://www.infoworld.com/article/3631197/agentic-ai-the-top-challenges-and-how-to-overcome-them.html","Key obstacles enterprises face when deploying agentic AI systems, including model logic, reliability, data privacy, and data quality","AI Agents, Enterprise AI, Data Privacy"
"3 Data Engineering Trends Riding Kafka, Flink, and Iceberg","InfoWorld","11/25/2024","https://www.infoworld.com/article/3607370/3-data-engineering-trends-riding-kafka-flink-and-iceberg.html","Emerging trends in the Apache Kafka, Flink, and Iceberg communities","Kafka, Flink, Iceberg, Data Engineering"
"Stream All the Things: Patterns of Effective Data Stream Processing","InfoQ","11/29/2024","https://www.infoq.com/news/2024/11/effective-data-stream-processing/","Key design patterns for managing data streaming challenges","Kafka, Stream Processing, Design Patterns"
"Implementing Data Fabric for Enhanced Business Operations","Forbes Tech Council","5/8/2023","https://www.forbes.com/councils/forbestechcouncil/2023/05/08/implementing-data-fabric-for-enhanced-business-operations-step-by-step/","A comprehensive guide to implementing data fabric architecture","Data Fabric, Data Architecture, Enterprise"
"Data Version Control: The Enabler of Data Engineering Best Practices","Forbes Tech Council","2/9/2023","https://www.forbes.com/councils/forbestechcouncil/2023/02/09/data-version-control-the-enabler-of-data-engineering-best-practices/","How data version control systems enable reproducibility and collaboration","Data Engineering, Version Control, Best Practices"
```

### Or in Table Format (paste into Google Sheets):

| title | publication | date | url | description | tags |
|-------|-------------|------|-----|-------------|------|
| Agentic AI: The Top Challenges and How to Overcome Them | InfoWorld | 1/7/2025 | https://www.infoworld.com/article/3631197/agentic-ai-the-top-challenges-and-how-to-overcome-them.html | Key obstacles enterprises face when deploying agentic AI systems | AI Agents, Enterprise AI |
| 3 Data Engineering Trends Riding Kafka, Flink, and Iceberg | InfoWorld | 11/25/2024 | https://www.infoworld.com/article/3607370/3-data-engineering-trends-riding-kafka-flink-and-iceberg.html | Emerging trends in the Apache Kafka, Flink, and Iceberg communities | Kafka, Flink, Iceberg |
| Stream All the Things: Patterns of Effective Data Stream Processing | InfoQ | 11/29/2024 | https://www.infoq.com/news/2024/11/effective-data-stream-processing/ | Key design patterns for managing data streaming challenges | Kafka, Stream Processing |

## Option 2: Local CSV File

Save this as `data/external-writing.csv`:

```csv
title,publication,date,url,description,tags
"Agentic AI: The Top Challenges and How to Overcome Them","InfoWorld","2025-01-07","https://www.infoworld.com/article/3631197/agentic-ai-the-top-challenges-and-how-to-overcome-them.html","Key obstacles enterprises face when deploying agentic AI systems, including model logic, reliability, data privacy, and data quality","AI Agents, Enterprise AI, Data Privacy, AI Reliability"
"3 Data Engineering Trends Riding Kafka, Flink, and Iceberg","InfoWorld","2024-11-25","https://www.infoworld.com/article/3607370/3-data-engineering-trends-riding-kafka-flink-and-iceberg.html","Emerging trends in the Apache Kafka, Flink, and Iceberg communities. Explores reimagining microservices with Flink streaming, leveraging SQL for real-time AI, and community-driven Iceberg innovations.","Kafka, Flink, Iceberg, Data Engineering"
"Stream All the Things: Patterns of Effective Data Stream Processing","InfoQ","2024-11-29","https://www.infoq.com/news/2024/11/effective-data-stream-processing/","Key design patterns for managing data streaming challenges. Covers exactly-once semantics, complex join operations between streams, and error management strategies for data integrity.","Kafka, Stream Processing, QCon, Design Patterns"
```

## Field Specifications

### title
- **Type**: Text
- **Required**: Yes
- **Example**: "Agentic AI: The Top Challenges and How to Overcome Them"
- **Notes**: Full article title as it appears on the publication

### publication
- **Type**: Text
- **Required**: Yes
- **Example**: "InfoWorld", "Forbes Tech Council", "InfoQ", "Confluent Blog"
- **Notes**: Name of the publication or platform

### date
- **Type**: Date
- **Required**: Yes
- **Format**: MM/DD/YYYY (will be converted to YYYY-MM-DD)
- **Example**: "1/7/2025" or "2025-01-07"
- **Notes**: Publication date of the article

### url
- **Type**: URL
- **Required**: Yes
- **Example**: "https://www.infoworld.com/article/..."
- **Notes**: Full URL to the article (must include https://)

### description
- **Type**: Text
- **Required**: Yes
- **Length**: 1-2 sentences (150-250 characters recommended)
- **Example**: "Key obstacles enterprises face when deploying agentic AI systems, including model logic, reliability, data privacy, and data quality."
- **Notes**: Brief summary of what the article covers

### tags
- **Type**: Comma-separated text
- **Required**: No (but recommended)
- **Example**: "AI Agents, Enterprise AI, Data Privacy"
- **Notes**: 3-5 relevant tags, separated by commas

## Tips

### Date Formatting
- Google Sheets: Use `1/7/2025` or `01/07/2025`
- CSV: Use `2025-01-07` (YYYY-MM-DD)
- Script will auto-convert to YYYY-MM-DD

### Tags Best Practices
- Use 3-5 tags per article
- Capitalize important terms (e.g., "AI Agents", "Kafka")
- Be consistent across articles
- Common tags: AI, Kafka, Flink, Data Engineering, Cloud, Leadership

### Description Guidelines
- Keep it concise (1-2 sentences)
- Focus on what readers will learn
- Use active voice
- No need to include "This article..." or "Learn about..."
- Start with the key benefit or insight

### URL Validation
- Always include full URL with `https://`
- Test each URL before adding
- Remove tracking parameters if desired (e.g., `?streamIndex=0`)

## Quick Copy-Paste Templates

### Template Row (Google Sheets)
```
[Article Title] | [Publication] | [MM/DD/YYYY] | [https://...] | [Brief description] | [tag1, tag2, tag3]
```

### Template Row (CSV)
```csv
"Article Title","Publication Name","YYYY-MM-DD","https://full-url.com","Brief description here","tag1, tag2, tag3"
```

---

## Ready to Use?

1. **Copy the example data above**
2. **Paste into Google Sheets** or save as CSV
3. **Add your own articles**
4. **Follow EXTERNAL-WRITING-SYNC.md** to set up the sync

---

Last Updated: 2026-03-12
