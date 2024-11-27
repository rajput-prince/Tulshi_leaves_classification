import os
from PIL import Image

# Function to convert all images to jpg and save them in a new folder
def convert_images_to_jpg(source_folder, destination_folder):
    # Check if the destination folder exists, if not create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        # Full path of the file
        file_path = os.path.join(source_folder, filename) 
        try:
            # Open the image using PIL
            with Image.open(file_path) as img:
                # Convert to RGB mode if the image has an alpha channel (transparency)
                if img.mode in ('RGBA', 'LA'):
                    img = img.convert('RGB')

                # Create a new file name with .jpg extension
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_file_path = os.path.join(destination_folder, new_filename)

                # Save the image as a .jpg file
                img.save(new_file_path, "JPEG")
                print(f"Converted {filename} to {new_filename}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")
    print("Image conversion completed.")

# Define the source folder path and destination folder path
source_folder = r"file_path"  # Change this to your input folder path
destination_folder = r"file_path"  # Change this to your output folder path

# Call the function to convert images to jpg
convert_images_to_jpg(source_folder, destination_folder)
