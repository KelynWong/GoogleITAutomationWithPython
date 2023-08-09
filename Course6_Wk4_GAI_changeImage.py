#! /usr/bin/env python3

from PIL import Image
import os

def process_images(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".tiff"):
            image_path = os.path.join(input_dir, filename)
            try:
                with Image.open(image_path) as img:
                    # Convert RGBA to RGB
                    img = img.convert("RGB")

                    # Resize the image
                    img = img.resize((600, 400))

                    # Change the format and save
                    new_filename = os.path.splitext(filename)[0] + ".jpeg"
                    output_path = os.path.join(output_dir, new_filename)
                    img.save(output_path, "JPEG")

                    print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = os.path.expanduser("~/supplier-data/images")
    output_directory = os.path.expanduser("~/supplier-data/images")

    process_images(input_directory, output_directory)
