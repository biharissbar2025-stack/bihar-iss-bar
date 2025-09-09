#!/bin/bash
# Setup project structure for Bihar Iss Bar

mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/election_commission
mkdir -p scrapers
mkdir -p utils

touch app.py requirements.txt
touch scrapers/twitter_scraper.py scrapers/youtube_scraper.py scrapers/news_scraper.py
touch utils/sentiment_analysis.py utils/weekly_summary.py utils/eci_parser.py

echo "streamlit
pandas
textblob
matplotlib
snscrape
newspaper3k" > requirements.txt

echo "Project structure created successfully!"
