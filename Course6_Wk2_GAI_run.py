#! /usr/bin/env python3

import os
import json
import requests

API_ENDPOINT = 'http://<ipAddress>/feedback/'

def process_feedback_files(folder_path):
    # List all .txt files in the feedback directory
    feedback_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    for feedback_file in feedback_files:
        file_path = os.path.join(folder_path, feedback_file)

        with open(file_path, 'r') as f:
            try:
                # Read and parse the content of the feedback file
                content = f.read()
                content_lines = content.strip().split('\n')

                # Create a dictionary from the content
                feedback_dict = {
                    'title': content_lines[0],
                    'name': content_lines[1],
                    'date': content_lines[2],
                    'feedback': "\n".join(content_lines[3:])
                }

                # Send data via API POST request
                response = requests.post(API_ENDPOINT, json=feedback_dict)

                if response.status_code == 201:
                    print(f"Feedback from {feedback_file} uploaded successfully.")
                else:
                    print(f"Error uploading feedback from {feedback_file}. Status code: {response.sta>
                    print("Response:", response.text)
            except Exception as e:
                print(f"Error processing {feedback_file}: {str(e)}")

if __name__ == "__main__":
    folder_path = "/data/feedback"
    process_feedback_files(folder_path)
