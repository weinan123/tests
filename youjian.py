import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication
class SendMail:
    def send_mail(self,title):
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = ''