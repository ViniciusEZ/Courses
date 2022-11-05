from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

my_email = '-----------'
my_password = '-----------'

with open('template1.html', 'r') as htm:
    template = Template(htm.read())
    current_date = datetime.now().strftime('%d/%m/%Y')
    msg_body = template.safe_substitute(name='Vinicius', date=current_date)


message = MIMEMultipart()
message['from'] = 'Vinicius Ezequiel'
message['to'] = my_email
message['subject'] = 'This email is a test. Sucessfully send!'
body1 = MIMEText(msg_body, 'html')
message.attach(body1)

with open('../day16/images/grand-canyon-colorado-river.jpg', 'rb') as imagem:
    imagem = MIMEImage(imagem.read())
    message.attach(imagem)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtpd:
    try:
        smtpd.ehlo()
        smtpd.starttls()
        smtpd.login(my_email, my_password)
        smtpd.send_message(message)
        print('E-mail send sucessfully.')
    except Exception as e:
        print('Email dont send...')
