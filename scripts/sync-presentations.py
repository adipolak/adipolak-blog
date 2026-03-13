#!/usr/bin/env python3
"""
Sync presentations from Google Sheets to YAML
"""

import os
import csv
import yaml
import requests
from datetime import datetime

def fetch_google_sheet(sheet_url):
    """Fetch CSV data from a published Google Sheet"""
    response = requests.get(sheet_url)
    response.raise_for_status()

    # Parse CSV
    lines = response.text.strip().split('\n')
    reader = csv.DictReader(lines)
    return list(reader)

def convert_to_presentation(row):
    """Convert a CSV row to presentation format"""
    # Parse date
    date_str = row.get('date', '')
    try:
        parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = parsed_date.strftime('%Y-%m-%d')
    except:
        formatted_date = date_str

    # Determine status (upcoming vs past)
    status = row.get('status', '').strip().lower()
    if not status:
        # Auto-determine from date if not provided
        try:
            talk_date = datetime.strptime(formatted_date, '%Y-%m-%d')
            status = 'upcoming' if talk_date >= datetime.now() else 'past'
        except:
            status = 'past'

    # Build presentation object
    presentation = {
        'title': row.get('title', '').strip(),
        'event': row.get('event', '').strip(),
        'date': formatted_date,
        'location': row.get('location', '').strip(),
        'description': row.get('description', '').strip(),
        'slides_url': row.get('slides_url', '').strip(),
        'video_url': row.get('video_url', '').strip(),
        'thumbnail': row.get('thumbnail', '').strip(),
        'status': status
    }

    # Remove empty fields (but keep status)
    return {k: v for k, v in presentation.items() if v not in ['', None] or k == 'status'}

def main():
    # Get sheet URL from environment (try both variable names)
    sheet_url = os.environ.get('SHEETS_URL') or os.environ.get('SHEET_URL')
    if not sheet_url:
        print("Error: SHEETS_URL environment variable not set")
        print("Usage: export SHEETS_URL='your-google-sheets-csv-url'")
        return

    print(f"Fetching data from Google Sheets...")
    rows = fetch_google_sheet(sheet_url)

    print(f"Found {len(rows)} presentations")

    # Convert to presentations format
    presentations = [convert_to_presentation(row) for row in rows]

    # Sort by date (newest first)
    presentations.sort(key=lambda x: x.get('date', ''), reverse=True)

    # Create YAML structure
    data = {
        'presentations': presentations
    }

    # Write to file
    output_path = 'data/presentations.yaml'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"✅ Updated {output_path} with {len(presentations)} presentations")

if __name__ == '__main__':
    main()
