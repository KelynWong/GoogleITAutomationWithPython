#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_data():
    data_directory = "supplier-data/descriptions"
    data = []

    for file_name in os.listdir(data_directory):
        if file_name.endswith(".txt"):
            with open(os.path.join(data_directory, file_name)) as f:
                lines = f.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                data.append((name, weight))

    return data

def main():
    data = process_data()
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(datetime.date.today())
    paragraph = data

    reports.generate_report(attachment, title, paragraph)

    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email("automation@example.com", "{}@example.com".format(os.environ.get('USER')), subject, body)
    emails.send_email(message)

if __name__ == "__main__":
    main()
