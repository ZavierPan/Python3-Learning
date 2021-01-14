# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))


# 需先至Google帳戶管理之安全性，開啟【低安全性應用程式存取權】，才能夠透過python寄信

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

sender_email = "renjie.python@gmail.com"  # Enter your address
password = "forpythontest"

receiver_email = "renjie.pan@theomnieyes.com"  # Enter receiver address

message = """\
Subject: Hi there

This message is sent from Python.

IPC public IP address is: {}
""".format(ip)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)