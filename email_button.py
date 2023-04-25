
import time
from gpiozero import Button
from gpiozero import MotionSensor


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from picamera import PiCamera

fromaddr = "megaproject000@gmail.com"
toaddr = "pankajmdahilkar@gmail.com"

def send_email(message):
       msg = MIMEMultipart()
       
       # storing the senders email address
       msg['From'] = fromaddr
       
       # storing the receivers email address
       msg['To'] = toaddr
       
       # storing the subject
       msg['Subject'] = "Mail From The Raspberry Pi"
       
       # string to store the body of the mail
       body = " following person at home" + message
       
       # attach the body with the msg instance
       msg.attach(MIMEText(body, 'plain'))
       
       # open the file to be sent
       filename = "img.jpg"
       attachment = open(filename, "rb")
       
       # instance of MIMEBase and named as p
       p = MIMEBase('application', 'octet-stream')
       
       # To change the payload into encoded form
       p.set_payload((attachment).read())
       
       # encode into base64
       encoders.encode_base64(p)
       
       p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
       
       # attach the instance 'p' to instance 'msg'
       msg.attach(p)
       
       # creates SMTP session
       s = smtplib.SMTP('smtp.gmail.com', 587)
       
       # start TLS for security
       s.starttls()
       
       # Authentication
       s.login(fromaddr, "earjgkyrfperupyf")
       
       # Converts the Multipart msg into a string
       text = msg.as_string()
       
       # sending the mail
       s.sendmail(fromaddr, toaddr, text)
       
       # terminating the session
       s.quit()
       print("mail sent")





button = Button(23)
pir = MotionSensor(24)

    

def loop():
        print("hello world")
        camera = PiCamera()
        time.sleep(2)
        print("Camrea initialized")
        while True:
              if button.is_pressed == True:
                  print("The button was pressed!")
                  print('Button Pressed...')
                  camera.capture("img.jpg")
                  send_email("Door bell pressed")
              if pir.motion_detected == True:
                  print('motion detect...')
                  pir.wait_for_no_motion()  
                  camera.capture("img.jpg")
                  send_email("motion detected") 
              time.sleep(0.2)
              #print('waiting...')
             
#setup()
loop()
