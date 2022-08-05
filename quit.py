import smtplib
from email.message import EmailMessage
import ssl
import sqlFuncs

# lpykkqlzwepalonk

def create_email(username, time, bad_posture):
    email_sender = 'whwhnshs@gmail.com'
    email_password = "lpykkqlzwepalonk"
    email_receiver = sqlFuncs.getEmailId(username)
    subject = "Session summary"
    body = f'''
    Total time worked: {time}
    Consistent bad posture maintained: {bad_posture} times
    '''
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())




