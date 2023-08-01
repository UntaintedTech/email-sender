import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'insert_your_name_here'
email['to'] = 'enter_name_@gmail.com'
email['subject'] = 'enter_subject_here!'

email.set_content('type your Message here')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('enter_your_email_@gmail.com', 'google_generated_password')# gmail apps_password is used
    smtp.send_message(email)
    print('Email sent!')




