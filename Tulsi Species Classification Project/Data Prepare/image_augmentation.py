import Augmentor
import os

# Define the pipeline for image augmentation
input_path = r"file_path"
output_path = os.path.join(input_path, "output")

# Ensure the output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Initialize the pipeline
p = Augmentor.Pipeline(input_path)

# Add image augmentations
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.3)
p.flip_left_right(probability=0.5)
p.rotate(probability=0.7, max_left_rotation=15, max_right_rotation=15)
p.skew(probability=0.5, magnitude=0.2)
p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=2)
p.random_brightness(probability=0.5, min_factor=0.7, max_factor=1.3)
p.random_contrast(probability=0.5, min_factor=0.8, max_factor=1.2)
p.resize(probability=1.0, width=512, height=512)

# Set the output image format
p.set_save_format("jpg")

# Generate samples
try:
    p.sample(800)
except FileNotFoundError as e:
    print(f"Error: {str(e)}. Ensure the directory exists and the file paths are correct.")
