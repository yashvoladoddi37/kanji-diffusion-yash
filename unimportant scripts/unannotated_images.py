import os
import shutil

# Define paths to the folders
folder1 = 'D:\sakana-ai\sakana-ai-2\data\kanji-jpg-path'  # Replace with the path to your first folder (JPG images)
folder2 = 'D:\sakana-ai\sakana-ai-2\data\kanji-png-path'  # Replace with the path to your second folder (PNG images)
output_folder = 'D:\sakana-ai\sakana-ai-2\data\kanji-unannotated-png'  # Replace with the path to the output folder

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get filenames without extensions for both folders
filenames1 = {os.path.splitext(f)[0] for f in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, f))}
filenames2 = {os.path.splitext(f)[0] for f in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, f))}

# Find filenames that are unique to each folder
unique_to_folder1 = filenames1 - filenames2
unique_to_folder2 = filenames2 - filenames1

# Copy unique images to the output folder
for filename in unique_to_folder1:
    jpg_file = os.path.join(folder1, filename + '.jpg')
    if os.path.exists(jpg_file):
        shutil.copy(jpg_file, output_folder)

for filename in unique_to_folder2:
    png_file = os.path.join(folder2, filename + '.png')
    if os.path.exists(png_file):
        shutil.copy(png_file, output_folder)

print("Unique files have been copied to the output folder.")
