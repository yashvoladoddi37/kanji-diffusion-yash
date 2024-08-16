import jsonlines
from collections import defaultdict

# Path to the JSONL file
jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_clean.jsonl"
merged_jsonl_path = "D:\sakana-ai\sakana-ai-2\kanji_dataset_clean_merge_duplicates.jsonl"

# Dictionary to store merged data
merged_data = defaultdict(list)

# Read the JSONL file and merge entries using jsonlines
with jsonlines.open(jsonl_path, mode='r') as reader:
    for obj in reader:
        file_name = obj['file_name']
        text = obj['text']
        
        # If it's the first occurrence, keep the full text
        if not merged_data[file_name]:
            merged_data[file_name].append(text)
        else:
            # For subsequent occurrences, remove "a Kanji meaning " and append the rest
            remaining_text = text.replace("a Kanji meaning ", "")
            merged_data[file_name].append(remaining_text)

# Write the merged data to a new JSONL file using jsonlines
with jsonlines.open(merged_jsonl_path, mode='w') as writer:
    for file_name, texts in merged_data.items():
        # Combine all texts into one, with " " separator
        combined_text = " ".join(texts)
        # Write the combined entry to the new file
        writer.write({"file_name": file_name, "text": combined_text})

print(f"Merged and cleaned JSONL file saved as: {merged_jsonl_path}")
