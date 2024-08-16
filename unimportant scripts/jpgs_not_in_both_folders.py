import os

# Define the paths to both folders
folder1 = "D:\sakana-ai\sakana-ai-2\kanji-jpg-path - Copy"
folder2 = "D:\sakana-ai\sakana-ai-2\kanji-jpg-path - Copy - Copy"

# Get sets of filenames from both folders (excluding file extensions)
filenames1 = {os.path.splitext(f)[0] for f in os.listdir(folder1) if f.endswith('.jpg')}
filenames2 = {os.path.splitext(f)[0] for f in os.listdir(folder2) if f.endswith('.jpg')}

# Find files present in folder1 but not in folder2
only_in_folder1 = filenames1 - filenames2

# Find files present in folder2 but not in folder1
only_in_folder2 = filenames2 - filenames1

# Output results
print(f"Files in {folder1} but not in {folder2}:")
for filename in only_in_folder1:
    print(filename + ".jpg")

print("\nFiles in {folder2} but not in {folder1}:")
for filename in only_in_folder2:
    print(filename + ".jpg")
