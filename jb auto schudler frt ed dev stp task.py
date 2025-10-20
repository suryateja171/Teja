import os
import schedule
import time
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
from googlesearch import search  


SENDER = "ramisettysuryateja9@gmail.com"
PASSWORD = "Surya@91600"
RECEIVER = "ramisettysuryateja9@gmail.com"

def job():
    query = "Daily frontend developer fresher India startups"
    links = list(search(query, tld="co.in", num=10, stop=10, pause=2))

    body = f"Job listings on {datetime.now():%Y-%m-%d}:\n\n"
    body += "\n".join(f"{i+1}. {l}" for i, l in enumerate(links))

    msg = MIMEText(body)
    msg["Subject"] = "Daily frontend developer Fresher Jobs in India"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER, PASSWORD)
            smtp.send_message(msg)
        print("Email sent!")
    except Exception as e:
        print("Failed to send:", e)

schedule.every().day.at("20:00").do(job)

print("Scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(60)

    
