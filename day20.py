# PYTHON AUTOMATION PROJECT: SEND EMAILS AUTOMATICALLY
import smtplib
from email.message import EmailMessage
# Email account details
sender_email = "your_email@gmail.com"
app_password = "your_16_character_app_password"
receiver_email = "receiver_email@example.com"
# Create the email
message = EmailMessage()
message["Subject"] = "Automatic Email from Python"
message["From"] = sender_email
message["To"] = receiver_email
message.set_content("""
Hello,
This email was sent automatically using Python.
Regards,
Python Automation
""")
# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(message)

    print("Email sent successfully!")

except Exception as error:
    print("Email could not be sent:", error)