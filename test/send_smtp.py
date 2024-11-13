import smtplib

server = smtplib.SMTP_SSL('smtp.ipage.com', 465)
server.set_debuglevel(1)  # Enable debug output
server.login('superset@ncc.com.la', 'Superset2024')
server.sendmail(
    'superset@ncc.com.la',
    'vilasackchaovichit@gmail.com',
    'Utilization exceeds 80%'
)
server.quit()
