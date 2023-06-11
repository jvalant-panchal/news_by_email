import smtplib
import ssl
import os

host = "smtp.gmail.com"
port = 465


def send_email(message):
    username = "elitesolutions.jp@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "elitesolutions.jp@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


