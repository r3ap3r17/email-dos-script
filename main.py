#This script will send email at desired address with message text provided in a file
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import threading

EMAIL = 'sender@email.com'         # Your email
PASSWORD = b'password'             # Base64 encoded password ( You can encode it with encoder.py)
MESSAGE = 'file.txt'               # File cotaining a message text
RECEIVER = 'reciever@email.com'    # Where you want to send your message
LEVEL = 500                        # Specify how many emails you want

class EmailAccount:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    #It decodes bs64 and returns it as a string
    def decoded_pass(self):
        return base64.b64decode(self.password, altchars=None).decode('utf-8')
    
    #Sends a email message
    def send_email(self, reciever, file):
        #reciever is a person ^ who recieves a email
        msg = MIMEMultipart()
        msg['From'] = 'PythonDevVB'
        msg['To'] = RECEIVER
        msg['subject'] = 'Just a test !'
        with open(file, 'r') as f:
            message = f.read()
        msg.attach(MIMEText(message, 'plain'))

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.ehlo()
                server.login(self.email, MyAcc.decoded_pass())
                server.sendmail(self.email, reciever, msg.as_string())
                server.quit()
                print('Message sent successfully !')
        except Exception as e:
            print(f'{e}\n\nMessage wasnt sent !')
    def threader(self, lvl):
        global threads
        threads=[]
        for i in range(1, int(lvl)):
            t=threading.Thread(target=MyAcc.send_email(RECEIVER, MESSAGE))
            threads.append(t)
            t.start()


#print(MyAcc.decoded_pass()) #Your password

MyAcc = EmailAccount(EMAIL, PASSWORD)
MyAcc.threader(LEVEL)
