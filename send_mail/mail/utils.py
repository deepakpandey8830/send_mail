import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.core.mail import send_mail

# Load email settings from config.json
def load_email_settings():
    config_path = os.path.join(settings.BASE_DIR, "config", "config.json")  # Use absolute path
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Send email using Django's send_mail function
def send_custom_email(subject, message, recipient_list, from_email=None):
    if not from_email:
        from_email = settings.EMAIL_HOST_USER
    
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False
    )

# Send email using SMTP manually
def send_contact_email(name, email, subject, message):
    try:
        email_settings = load_email_settings()
        
        msg = MIMEMultipart()
        msg["From"] = email_settings["EMAIL_HOST_USER"]
        msg["To"] = email_settings["EMAIL_HOST_USER"]  # Sending to self (Modify if needed)
        msg["Subject"] = subject

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, "plain"))

        # Setup SMTP connection
        server = smtplib.SMTP(email_settings["EMAIL_HOST"], email_settings["EMAIL_PORT"])
        server.starttls()
        server.login(email_settings["EMAIL_HOST_USER"], email_settings["EMAIL_HOST_PASSWORD"])
        
        # Send email
        server.sendmail(email_settings["EMAIL_HOST_USER"], email_settings["EMAIL_HOST_USER"], msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Email sending failed: {str(e)}")  # Log error properly
        return False
