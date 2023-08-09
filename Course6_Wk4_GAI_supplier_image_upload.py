#! /usr/bin/env python3

import os
import requests

def upload_images(image_dir, url):
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpeg"):
            image_path = os.path.join(image_dir, filename)
            with open(image_path, 'rb') as opened:
                response = requests.post(url, files={'file': opened})

                if response.status_code == 201:
                    print(f"Uploaded {filename} successfully")
                else:
                    print(f"Failed to upload {filename}, Status code: {response.status_code}")

if __name__ == "__main__":
    image_directory = os.path.expanduser("~/supplier-data/images")
    upload_url = "http://localhost/upload/"

    upload_images(image_directory, upload_url)
