import json
import os

# Path to the directory containing the 5082 images
images_dir = "D:\sakana-ai\sakana-ai-2\kanji-jpg-path"

# Path to the JSONL file
jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_clean.jsonl"
cleaned_jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_cleaned.jsonl"  # Output path for cleaned JSONL file

# Load the valid JPG filenames into a set (excluding file extensions)
valid_filenames = {os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.endswith('.jpg')}

# Process the JSONL file and keep only valid entries
with open(jsonl_path, 'r') as input_file, open(cleaned_jsonl_path, 'w') as output_file:
    for line in input_file:
        data = json.loads(line)
        # Check if the file_name (excluding extension) is in the valid_filenames set
        if os.path.splitext(data['file_name'])[0] in valid_filenames:
            output_file.write(json.dumps(data) + "\n")

print(f"Cleaning completed. Cleaned JSONL file saved as: {cleaned_jsonl_path}")
