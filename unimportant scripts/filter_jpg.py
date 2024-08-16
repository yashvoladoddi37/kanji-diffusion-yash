import os
jpg_dir = 'D:\sakana-ai\sakana-ai-2\kanji-jpg-path'
metadata_file_path = 'D:\sakana-ai\sakana-ai-2\kanji_dataset_clean.jsonl'
for jpg_file in os.listdir(jpg_dir):
    if jpg_file.endswith('.jpg'):
        with open(metadata_file_path, 'r') as metadata:
            if jpg_file not in metadata.read():
                os.remove(os.path.join(jpg_dir, jpg_file))