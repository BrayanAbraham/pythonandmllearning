import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'brayanabraham@gmail.com' 
msg.set_content('How about dinner at 6pm this saturday?')

files = ['01-mercedes-amg-gt-r-c-190-wallpaper-3840x2160.jpg','IMG_20181102_151528_407.jpg']

for file in files:
	with open(file,'rb') as f:
		file_data = f.read()
		file_type = imghdr.what(f.name)
		file_name = f.name

	msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

# for other files maintype = 'application' subtype = 'octect-stream' and remove file_type from with statement

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

	smtp.send_message(msg)


#TO SEND OUT MAIL WITHOUT SSL
# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
# 	smtp.ehlo() #identify ourself with mail server
#  	smtp.starttls() #encrypt traffic
#  	smtp.ehlo()
#  	smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
	
# 	subject = 'Grab dinner this weekend?'
# 	body = 'How about dinner at 6pm this saturday?'

# 	msg = 'Subject: {}\n\n{}'.format(subject,body)

# 	smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


#TO TEST AT LOCALHOST
# with smtplib.SMTP('localhost',1025) as smtp:
# 	subject = 'Grab dinner this weekend?'
# 	body = 'How about dinner at 6pm this saturday?'

# 	msg = 'Subject: {}\n\n{}'.format(subject,body)

# 	smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)