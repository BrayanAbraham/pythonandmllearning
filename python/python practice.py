import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Mail using python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'kuldipwork3@gmail.com','brayanabraham@gmail.com' 
msg.set_content('Kyu pareshaan kar raha hai? \n shaanti se jeene nahi de sakta kya? \n Tu python k alawa aur kahin se mail nahi lega hain be\n agar aisi harkat phir ki toh ghar aa ke marunga \n\nWith Love\nBrayan Abraham')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)