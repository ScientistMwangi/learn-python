from pathlib import Path
import smtplib
from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

message = MIMEMultipart()
message["from"] = "Samuel Mwangi"
message["to"] = "scientistmwangi@gmail.com"
message["subject"] = "Test Python Mail"

# attach body
message.attach(MIMEText("body"))
message.attach(MIMEImage(Path("book1.jfif").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Email and Password
    # Should be in try and catch
    smtp.login("", "")
    smtp.send_message(message)
    print("sent...")
