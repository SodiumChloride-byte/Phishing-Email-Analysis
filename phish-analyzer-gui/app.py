from flask import Flask, render_template, request
import re
from email import message_from_string
from urllib.parse import urlparse

app = Flask(__name__)

def analyze_email(raw_text):
    msg = message_from_string(raw_text)
    results = {
        "from": msg.get("From", ""),
        "subject": msg.get("Subject", ""),
        "email_address": "",
        "links": [],
        "has_attachments": False,
        "suspicious_indicators": []
    }

    # extract email address from From header
    m = re.search(r'[\w\.-]+@[\w\.-]+', results["from"])
    if m:
        results["email_address"] = m.group(0)

    # get body (plain text)
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and part.get_content_disposition() != "attachment":
                try:
                    body += part.get_payload(decode=True).decode("utf-8", errors="replace")
                except:
                    body += str(part.get_payload())
            if part.get_content_disposition() == "attachment":
                results["has_attachments"] = True
    else:
        try:
            body = msg.get_payload(decode=True).decode("utf-8", errors="replace")
        except:
            body = str(msg.get_payload())

    results["body_snippet"] = body[:2000]

    # find links
    links = re.findall(r'https?://[^\s<>")]+|www\.[^\s<>")]+', body)
    results["links"] = links

    suspicious = []

    # simple heuristics
    if re.search(r'\burgent\b|\bimmediate\b|verify your account|account will be closed', body, re.I):
        suspicious.append("uses urgent or threatening language")

    if "no-reply" in results["from"].lower() or "admin" in results["from"].lower():
        suspicious.append("generic/role sender (no-reply/admin)")

    for link in links:
        parsed = urlparse(link if link.startswith("http") else "http://" + link)
        # IP in netloc
        hostname = parsed.hostname or ""
        if re.match(r'^\d+\.\d+\.\d+\.\d+$', hostname):
            suspicious.append("link uses IP address")
        # suspicious tlds (example list)
        if hostname and hostname.split(".")[-1] in ("xyz","top","ru","cn"):
            suspicious.append(f"link uses uncommon TLD: .{hostname.split('.')[-1]}")

    if results["has_attachments"]:
        suspicious.append("contains attachment(s)")

    # dedupe
    results["suspicious_indicators"] = list(dict.fromkeys(suspicious))
    return results

@app.route("/", methods=["GET","POST"])
def index():
    report = None
    raw = ""
    if request.method == "POST":
        uploaded = request.files.get("file")
        if uploaded and uploaded.filename != "":
            raw = uploaded.read().decode("utf-8", errors="replace")
        else:
            raw = request.form.get("raw_email", "")
        if raw.strip():
            report = analyze_email(raw)
    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
