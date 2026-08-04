import csv

import os

from dotenv import load_dotenv

from email_sender import send_email

from email_template import create_email

from logger import write_log


load_dotenv()


EMAIL = os.getenv("EMAIL_ADDRESS")

PASSWORD = os.getenv("EMAIL_PASSWORD")


with open("data/customers.csv", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"]

        receiver = row["email"]

        subject, body = create_email(name)

        success = send_email(
            EMAIL,
            PASSWORD,
            receiver,
            subject,
            body,
        )

        if success:

            print(f"Email sent to {name}")

            write_log(f"SUCCESS -> {receiver}")

        else:

            print(f"Failed to send to {name}")

            write_log(f"FAILED -> {receiver}")