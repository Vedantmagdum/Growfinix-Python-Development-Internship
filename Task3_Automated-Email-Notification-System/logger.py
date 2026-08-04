from datetime import datetime

LOG_FILE = "logs/email_log.txt"


def write_log(message):

    with open(LOG_FILE, "a") as file:

        current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{current}] {message}\n")