from email.mime.multipart import MIMEMultipart
import logging
import os
import smtplib
from email.mime.text import MIMEText

logger = logging.getLogger("mailer.py")

SENDER_EMAIL = str(os.getenv("EMAIL_USER"))
APP_PASSWORD = str(os.getenv("EMAIL_PASS"))  # your App Password
HOST = str(os.getenv("SMTP_SERVER"))
PORT = str(os.getenv("SMTP_PORT"))


def send_email(row):
    receiver = row["email_id"]

    msg_text = ""
    subject_text = ""
    if row["room_type"] == "WG":
        with open("templates\\wg-template.txt", "r", encoding="utf-8") as file:
            msg_text = file.read()
            subject_text = "Inquiry about the WG Room availability"
    elif row["no_of_rooms"] > 1:
        with open("templates\\other-template.txt", "r", encoding="utf-8") as file:
            msg_text = file.read()
            subject_text = "Inquiry about the apartment availability"
    elif row["no_of_rooms"] == 1:
        with open("templates\\1room-template.txt", "r", encoding="utf-8") as file:
            msg_text = file.read()
            subject_text = "Inquiry about the apartment availability"

    formatted_msg_text = msg_text.format(
        firstname=row["landlord_first_name"],
        lastname=row["landlord_last_name"],
        street=row["street"],
        city=row["city"],
    )

    msg = MIMEMultipart()
    msg.attach(MIMEText(formatted_msg_text, "plain", "utf-8"))
    msg["Subject"] = subject_text
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver

    # logger.debug(formatted_msg_text)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

    logger.info("✅ Email sent successfully!")
