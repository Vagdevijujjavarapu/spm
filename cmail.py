import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('vagdevijujjavarapu15@gamil.com ','quftxlposcwxmwpo')
    msg=EmailMessage()
    msg['From']='vagdevijujjavarapu15@gamil.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

    







        
    
