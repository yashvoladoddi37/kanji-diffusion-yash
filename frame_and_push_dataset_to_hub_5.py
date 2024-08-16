import jsonlines
from datasets import load_dataset, DatasetDict
import os
# Paths
jpg_dir = "D:\\sakana-ai\\sakana-ai-2\\kanji-jpg-path"
jsonl_file_path = os.path.join(jpg_dir, "kanji_caption_dataset.jsonl")

# Load image data
image_dataset = load_dataset("imagefolder", data_dir=jpg_dir, split="train")

# Load the JSONL file
text_data = {}
with jsonlines.open(jsonl_file_path) as reader:
    for obj in reader:
        # Normalize the filename
        normalized_filename = obj["file_name"].strip().lower()
        text_data[normalized_filename] = obj["text"]

# Merge image data with text data
def add_text(example):
    # Normalize the filename from the image dataset
    # image_filename = example['image'].filename.split('/')[-1].strip().lower()
    # Extract just the filename from the full path and normalize it
    image_filename = os.path.basename(example['image'].filename).strip().lower()
    
    # Try to find a match in text_data
    matching_key = next((key for key in text_data if key in image_filename), None)

    if matching_key:
        example['text'] = text_data[image_filename]
    else:
        example['text'] = ""
        print(f"Warning: No text found for {image_filename}")

    return example

# Apply the merging function
dataset_with_text = image_dataset.map(add_text)

# Verify the dataset structure
print(dataset_with_text[:5])

# Push the dataset to Hugging Face Hub
dataset_with_text.push_to_hub("yashvoladoddi37/kanjienglish")
