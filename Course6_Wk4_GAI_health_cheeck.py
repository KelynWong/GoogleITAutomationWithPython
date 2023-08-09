#!/usr/bin/env python3

import os
import time
import socket
import psutil
from emails import generate_email, send_email

# Configuration
sender_email = "automation@example.com"
recipient_email = "{}@example.com".format(os.environ.get('USER'))

def check_cpu_usage():
    return psutil.cpu_percent(interval=1) > 80

def check_disk_space():
    disk = psutil.disk_usage("/")
    return disk.percent > 80

def check_memory():
    memory = psutil.virtual_memory()
    return memory.available < 500 * 1024 * 1024  # 500MB in bytes

def check_hostname_resolution():
    try:
        return socket.gethostbyname("localhost") != "127.0.0.1"
    except socket.gaierror:
        return True

def generate_error_report(errors):
    return "\n".join([f"Error - {error}" for error in errors])

def main():
    while True:
        errors = []
        subject = ["Error - "]

        if check_cpu_usage():
            errors.append("CPU usage is over 80%")
            subject.append("CPU usage is over 80%")

        if check_disk_space():
            errors.append("Available disk space is lower than 20%")
            subject.append("Available disk space lower than 20%")

        if check_memory():
            errors.append("Available memory is less than 500MB")
            subject.append("Available memory is less than 500MB")

        if check_hostname_resolution():
            errors.append('Hostname "localhost" cannot be resolved to "127.0.0.1"')
            subject.append("localhost cannot be resolved to 127.0.0.1")

        if errors:
            error_report = generate_error_report(errors)
            email_subject = " ".join(subject)
            email_body = "Please check your system and resolve the issue as soon as possible."
            email_message = generate_email(sender_email, recipient_email, email_subject, email_body)

            send_email(email_message)
            print("Email sent for the following issues:\n", "\n".join(errors))

        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()
