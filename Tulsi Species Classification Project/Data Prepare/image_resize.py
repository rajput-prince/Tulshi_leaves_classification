import os
from PIL import Image

# Define the paths
input_folder = r"file_path"  # Replace with your input folder path
output_folder = r"file_path"  # Replace with your output folder path

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set the size for resizing
size = (256, 256)

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):  # Specify the image formats you want to process
        # Open the image
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            # Resize the image
            img_resized = img.resize(size)
            
            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)

print("All images have been resized and saved.")
