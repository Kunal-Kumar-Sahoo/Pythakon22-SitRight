import smtplib
from email.message import EmailMessage
import ssl
import csv

# lpykkqlzwepalonk

def getPenalties(username):
    file = open('data.csv', 'r')
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        if username in line:
            return line[-1]
def getEmail(username):
    file = open('data.csv', 'r')
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        if username in line:
            return line[2]

def sendEmail(username, time):
    email_sender = 'whwhnshs@gmail.com'
    email_password = "lpykkqlzwepalonk"
    email_receiver = getEmail(username)
    subject = "Session summary"
    body = f'''
    Total time worked: {time}
    Consistent bad posture maintained: {getPenalties(username)} times
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



if __name__ == '__main__':
    sendEmail('Dev', getEmail('Dev'), 10, 69)