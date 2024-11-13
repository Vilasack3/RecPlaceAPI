import smtplib
from email.mime.text import MIMEText

# Email details
from_address = "superset@ncc.com.la"
to_address = "vilasackchaovichit@gmail.com"
subject = "Test Email from Python"
body = "Utilization exceeds 80%"

# SMTP server configuration
smtp_server = "smtp.ipage.com"  # Replace with your SMTP server
smtp_port = 587  # Typically 587 for STARTTLS, or 465 for SSL/TLS
username = "superset@ncc.com.la"
password = "Superset2024"

# Compose and send email
msg = MIMEText(body)
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable encryption for STARTTLS
    server.login(username, password)
    server.sendmail(from_address, to_address, msg.as_string())
    print("Email sent successfully.")
    print(f"Body: {body}")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
