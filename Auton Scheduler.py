import os
import schedule
import time
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import csv
from googlesearch import search

# -------------------------
# Configuration (use env vars for security)
# -------------------------
SENDER = os.getenv("EMAIL_USER", "yourmail@gmail.com")
PASSWORD = os.getenv("EMAIL_PASS", "Suryateja@91600")   # Use Gmail App Password
RECEIVER = "ramisettysuryateja9@gmail.com"

# -------------------------
# Job function
# -------------------------
def job():
    try:
        query = "DevOps Engineer fresher India MNCS"
        links = list(search(query, tld="co.in", num=10, stop=10, pause=2))

        # Build email body
        body = f"Job listings on {datetime.now():%Y-%m-%d}:\n\n"
        body += "\n".join(f"{i+1}. {l}" for i, l in enumerate(links))

        # Save to CSV file
        with open("jobs.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for i, link in enumerate(links):
                writer.writerow([datetime.now().strftime("%Y-%m-%d"), i+1, link])

        # Create email
        msg = MIMEText(body)
        msg["Subject"] = "Daily DevOps Fresher Jobs in India"
        msg["From"] = SENDER
        msg["To"] = RECEIVER

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER, PASSWORD)
            smtp.send_message(msg)

        print("✅ Email sent & jobs saved to CSV!")

    except Exception as e:
        print("❌ Failed to send:", e)

# -------------------------
# Scheduler
# -------------------------
schedule.every().day.at("23:00").do(job)

print("Scheduler started... Waiting for 22:00 daily")
while True:
    schedule.run_pending()
    time.sleep(60)
