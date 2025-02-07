import smtplib
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'damolabalogun79@gmail.com'
    password = os.getenv('PASSWORD')
    receiver = 'damolabalogun@gmail.com'
    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    mail_message = """\
Subject: Greeting

Hello t6his is Damola writing code   
    """
    send_email(mail_message)