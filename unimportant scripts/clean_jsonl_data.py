import os
import json
import re

# Define the paths
jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset.jsonl"
cleaned_jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_clean.jsonl"

# Regular expression to remove the suffix after the hyphen
pattern = re.compile(r'-[^.]+')  # Matches '-' followed by any characters until the extension

# Process the JSONL file
with open(jsonl_path, 'r') as input_file, open(cleaned_jsonl_path, 'w') as output_file:
    for line in input_file:
        data = json.loads(line)
        # Remove the suffix after the hyphen
        data['file_name'] = pattern.sub('', data['file_name'])
        # Write the cleaned entry to the new file
        output_file.write(json.dumps(data) + "\n")

print("JSONL cleaning completed. Cleaned JSONL file saved as:", cleaned_jsonl_path)
