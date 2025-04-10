import smtplib
import ssl


def send_email(message):
    #Step 1: Set the host string and port number integer
    host = "smtp.gmail.com"
    port = 465

    #Step 2: Get an App password from gmail
    #Step 3: Set the sending email(username) and password of that account and set the receiver email
    username = "imjogiat@gmail.com"
    password = "iutv xhxw zjpo sbwu"
    receive_email = "imjogiat@gmail.com"

    #Step 4: define a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as mailserver:
        mailserver.login(username, password)
        mailserver.sendmail(username, receive_email, message)