import smtplib

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders


def sendEmail(fromAddr: str, toAddr: str, password: str, subject: str, body: str, files: list()) -> object:
    '''
    Send .docx from fromAddr to toAddr
    :param fromAddr: what address you send from. Make sure to enable lesser app access
    :type fromAddr: str
    :param toAddr:  where addresss ur sending email to
    :type toAddr: str
    :param password: password for fromAddr
    :type password: str
    :param subject: for subject in email
    :type subject: str
    :param body: for body in email
    :type body: str
    :param files: of filePath for .docx document
    :type files: list(str)
    :return: None
    '''
    # Define our sender and recipient addresses

    # MSG Object
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg['To'] = toAddr
    msg['Subject'] = subject

    # Add Body
    msg.attach(MIMEText(body))

    # Add .docx attachment
    for filename in files:
        attachment = open(filename, 'rb')
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        msg.attach(part)
    msg = msg.as_string()

    # Send Email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(fromAddr, password)
        server.sendmail(fromAddr, toAddr, msg)
        server.quit()
        print('Email sent successfully')
    except:
        print("Email couldn't be sent")
