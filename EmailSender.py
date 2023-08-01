import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Kuya Wil'
email['to'] = 'tine.literal@gmail.com'
email['subject'] = 'Nanalo ka ng sampong libo!'

email.set_content('dubidubidapdap ang sabi ng dyip beep 3x')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jpatricksemillano@gmail.com', 'gzemydnameqrulbn')# gmail apps_password is used
    smtp.send_message(email)
    print('sampong libo!')




