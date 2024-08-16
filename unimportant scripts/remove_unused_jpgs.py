import os
import json

# Define the paths
images_dir = "D:\sakana-ai\sakana-ai-2\kanji-jpg-path - Copy"
jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_clean.jsonl"

# Load filenames from the JSONL file into a set
json_filenames = set()

with open(jsonl_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        json_filenames.add(data['file_name'])

# Iterate through the image folder and remove images without corresponding text
for image_filename in os.listdir(images_dir):
    if image_filename not in json_filenames:
        os.remove(os.path.join(images_dir, image_filename))
        print(f"Removed: {image_filename}")

print("Cleaning completed.")
