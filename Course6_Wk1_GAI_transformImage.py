#!/usr/bin/env python3

from PIL import Image
import os

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        print(filename)
        if filename.endswith('48dp'):
            print("here2")
            # Open the image file
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Rotate the image 90° clockwise
            img = img.rotate(-90, expand=True)

            # Convert the image to RGB mode if it's not already
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Resize the image from 192x192 to 128x128
            img = img.resize((128, 128))

            # Save the image to the output folder in .jpeg format
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpeg')
            img.save(output_path, 'JPEG')

            # Close the image
            img.close()

if _name_ == "_main_":
    input_folder = "./images" 
    output_folder = "/opt/icons/" 

    process_images(input_folder, output_folder)
