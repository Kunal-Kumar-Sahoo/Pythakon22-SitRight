import smtplib
from email.message import EmailMessage
import ssl

# lpykkqlzwepalonk

email_sender = 'whwhnshs@gmail.com'
email_password = 'lpykkqlzwepalonk'
email_receiver = 'parikhdev13@gmail.com'
em = EmailMessage()


def create_email():
    subject = "Session summary"
    body = """
    sfjhsvefkgwewjhfevkhw
    """

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)


def send_email():
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def final_email():
    create_email()
    send_email()


final_email()