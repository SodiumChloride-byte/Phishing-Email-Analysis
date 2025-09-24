# Phish Analyzer GUI

Simple Flask web app to analyze a raw email (.eml or pasted headers+body) and show basic phishing indicators.

## Run locally
1. Create a Python 3.8+ virtual environment:
   python3 -m venv venv
   source venv/bin/activate
2. Install:
   pip install -r requirements.txt
3. Run:
   python app.py
4. Open http://127.0.0.1:5000

## Repo structure
- app.py: Flask app and analysis logic
- templates/: HTML template
- samples/: example .eml files
- REPORT.md: report template for submission

## License
MIT
