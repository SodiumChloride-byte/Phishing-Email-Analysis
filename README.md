# Phish Analyzer GUI

A simple Flask web app that analyzes raw emails (`.eml` files or pasted text) and highlights potential phishing indicators such as suspicious sender addresses, urgent wording, links, and attachments.

---

## Features
- Upload or paste raw emails.  
- Extracts sender, subject, links, and attachments.  
- Flags suspicious patterns (urgent language, IP-based links, uncommon TLDs, role-based senders).  
- Clean Bootstrap-based web interface.  

---

## Getting Started

### Requirements
- Python 3.8+  
- pip  

### Installation
```bash
git clone https://github.com/YOURUSER/phish-analyzer-gui.git
cd phish-analyzer-gui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run
```bash
python app.py
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Deployment

### Render
1. Push this repo to GitHub.  
2. On [Render](https://render.com), create a new Web Service from your repo.  
3. Build Command:
   ```
   pip install -r requirements.txt
   ```
   Start Command:
   ```
   python app.py
   ```
   Port: 5000  

Render will give you a live URL.

### Heroku (optional)
Add a `Procfile`:
```
web: python app.py
```
Then push with:
```bash
heroku create
git push heroku main
```

---

## Repo Structure
```
phish-analyzer-gui/
├─ app.py                # Flask backend + analysis logic
├─ templates/index.html  # Frontend (Bootstrap)
├─ samples/sample-phish.eml
├─ REPORT.md             # Report template
├─ requirements.txt
├─ .github/workflows/    # CI workflow
├─ Dockerfile
├─ README.md
└─ LICENSE
```

---

## Example Usage
1. Upload `samples/sample-phish.eml`.  
2. The analyzer flags:  
   - Sender: `no-reply@secure-alerts.xyz` (role-based, uncommon TLD).  
   - Urgent wording: “verify your account immediately.”  
   - Link with IP: `http://192.0.2.1/login`.  
   - Attachment: none.  

---

## Deliverables for Submission
- **Code**: in this repo.  
- **Sample dataset**: `samples/sample-phish.eml`.  
- **Screenshots**: add GUI screenshots under `static/screenshots/`.  
- **Report**: fill in `REPORT.md` with findings for your chosen samples.  

---
