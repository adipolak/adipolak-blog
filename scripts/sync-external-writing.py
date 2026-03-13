#!/usr/bin/env python3
"""
Sync external writing articles from Google Sheets CSV to YAML

This script fetches a CSV from a Google Sheet and converts it to the
external-writing.yaml format used by Hugo.

Usage:
    SHEETS_URL="https://docs.google.com/spreadsheets/d/.../export?format=csv" python3 scripts/sync-external-writing.py

Environment Variables:
    SHEETS_URL or SHEET_URL: Google Sheets CSV export URL
"""

import os
import sys
import requests
import csv
from datetime import datetime
from io import StringIO

def fetch_csv_from_sheets(url):
    """Fetch CSV data from Google Sheets export URL"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_csv_to_articles(csv_text):
    """Parse CSV text into article dictionaries"""
    articles = []
    csv_reader = csv.DictReader(StringIO(csv_text))

    for row in csv_reader:
        # Skip empty rows
        if not row.get('title', '').strip():
            continue

        # Parse date
        date_str = row.get('date', '').strip()
        try:
            if date_str:
                # Try to parse the date and format it as YYYY-MM-DD
                parsed_date = datetime.strptime(date_str, '%m/%d/%Y')
                formatted_date = parsed_date.strftime('%Y-%m-%d')
            else:
                formatted_date = ''
        except ValueError:
            # If date is already in YYYY-MM-DD format or invalid
            formatted_date = date_str

        # Parse tags (comma-separated)
        tags_str = row.get('tags', '').strip()
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]

        article = {
            'title': row.get('title', '').strip(),
            'publication': row.get('publication', '').strip(),
            'date': formatted_date,
            'url': row.get('url', '').strip(),
            'description': row.get('description', '').strip(),
            'tags': tags
        }

        articles.append(article)

    return articles

def generate_yaml(articles):
    """Generate YAML content from articles list"""
    yaml_lines = [
        "# External Writing & Publications",
        "#",
        "# Articles published on other platforms and publications",
        "# This file is synced from Google Sheets - DO NOT EDIT MANUALLY",
        "# Use scripts/sync-external-writing.py to update",
        "",
        "articles:"
    ]

    # Group articles by year for better organization
    articles_by_year = {}
    for article in articles:
        if article['date']:
            year = article['date'][:4]
            if year not in articles_by_year:
                articles_by_year[year] = []
            articles_by_year[year].append(article)

    # Sort years in descending order
    for year in sorted(articles_by_year.keys(), reverse=True):
        yaml_lines.append(f"  # {year}")

        for article in articles_by_year[year]:
            yaml_lines.append(f'  - title: "{article["title"]}"')
            yaml_lines.append(f'    publication: "{article["publication"]}"')
            yaml_lines.append(f'    date: "{article["date"]}"')
            yaml_lines.append(f'    url: "{article["url"]}"')
            yaml_lines.append(f'    description: "{article["description"]}"')

            if article['tags']:
                tags_str = ', '.join([f'"{tag}"' for tag in article['tags']])
                yaml_lines.append(f'    tags: [{tags_str}]')
            else:
                yaml_lines.append('    tags: []')
            yaml_lines.append('')

    return '\n'.join(yaml_lines)

def main():
    # Get Google Sheets URL from environment (support both SHEETS_URL and SHEET_URL)
    sheets_url = os.environ.get('SHEETS_URL') or os.environ.get('SHEET_URL')

    if not sheets_url:
        print("Error: SHEETS_URL environment variable not set", file=sys.stderr)
        print("", file=sys.stderr)
        print("Usage:", file=sys.stderr)
        print('  SHEETS_URL="https://docs.google.com/.../export?format=csv" python3 scripts/sync-external-writing.py', file=sys.stderr)
        sys.exit(1)

    print(f"Fetching CSV from Google Sheets...")
    csv_text = fetch_csv_from_sheets(sheets_url)

    print("Parsing articles...")
    articles = parse_csv_to_articles(csv_text)
    print(f"Found {len(articles)} articles")

    print("Generating YAML...")
    yaml_content = generate_yaml(articles)

    # Write to file
    output_file = 'data/external-writing.yaml'
    with open(output_file, 'w') as f:
        f.write(yaml_content)

    print(f"✓ Successfully synced {len(articles)} articles to {output_file}")
    print("")
    print("Article summary:")
    for article in articles[:5]:  # Show first 5
        print(f"  • {article['title']} ({article['publication']}, {article['date']})")
    if len(articles) > 5:
        print(f"  ... and {len(articles) - 5} more")

if __name__ == '__main__':
    main()
