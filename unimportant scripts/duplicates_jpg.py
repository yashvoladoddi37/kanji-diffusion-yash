import json

# Path to the JSONL file
jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_clean.jsonl"

# Set to store unique filenames
unique_filenames = set()

# List to store duplicates
duplicate_filenames = []

# Process the JSONL file
with open(jsonl_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        filename = data['file_name']
        
        # Check for duplicates
        if filename in unique_filenames:
            duplicate_filenames.append(filename)
        else:
            unique_filenames.add(filename)

# Output results
if duplicate_filenames:
    print(f"Found {len(duplicate_filenames)} duplicate filenames:")
    # for filename in duplicate_filenames:
    #     print(filename)
else:
    print("No duplicate filenames found.")
