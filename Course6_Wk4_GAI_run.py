#! /usr/bin/env python3

import os
import requests

def process_txt_files(description_dir):
    fruits_data = []

    for filename in os.listdir(description_dir):
        if filename.endswith(".txt"):
            txt_path = os.path.join(description_dir, filename)
            with open(txt_path, 'r') as txt_file:
                lines = txt_file.readlines()

                name = lines[0].strip()
                weight = int(lines[1].strip().split()[0])  # Extracting weight as an integer
                description = lines[2].strip()
                image_name = os.path.splitext(filename)[0] + ".jpeg"

                fruit_data = {
                    "name": name,
                    "weight": weight,
                    "description": description,
                    "image_name": image_name
                }
                fruits_data.append(fruit_data)

    return fruits_data

def upload_fruits_data(fruits_data, url):
    for fruit in fruits_data:
        response = requests.post(url, json=fruit)

        if response.status_code == 201:
            print(f"Uploaded {fruit['name']} successfully")
        else:
            print(f"Failed to upload {fruit['name']}, Status code: {response.status_code}")

if __name__== "__main__":
    description_directory = os.path.expanduser("~/supplier-data/descriptions")
    upload_url = "http://<ipAddress>/fruits/"

    fruits_data = process_txt_files(description_directory)
    upload_fruits_data(fruits_data, upload_url)
