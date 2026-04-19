import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def yuborish_email():
    # Email manzillari
    manzil = "sender@example.com"
    manzil_qabul = "receiver@example.com"

    # Email xabarining matni
    xabar = "Test email xabari"

    # Email manzillari va xabari
    msg = MIMEMultipart()
    msg['From'] = manzil
    msg['To'] = manzil_qabul
    msg['Subject'] = "Test email"
    msg.attach(MIMEText(xabar, 'plain'))

    # Smtplib orqali email yuborish
    server = smtplib.SMTP('localhost')
    server.sendmail(manzil, manzil_qabul, msg.as_string())
    server.quit()

yuborish_email()
