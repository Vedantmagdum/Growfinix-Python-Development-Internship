import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


def send_email(sender, password, receiver, subject, body):

    try:

        message = MIMEMultipart()

        message["From"] = sender

        message["To"] = receiver

        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender, password)

        server.sendmail(sender, receiver, message.as_string())

        server.quit()

        return True

    except Exception as e:

        print(e)

        return False