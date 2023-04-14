import os
import shutil

src_dir = "/Users/moki/Music/Music/Media.localized/Music/"
dest_dir = "../data/tracks"

# Check if the destination directory exists, if not, create it
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Iterate through the source directory and its subfolders to find MP3 files
mp3_count = 0
for root, dirs, files in os.walk(src_dir):
    print(f"Checking in directory: {root}")
    for file in files:
        print(f"Found file: {file}")
        # Check if the file has the .mp3 extension
        if file.endswith(".mp3"):
            mp3_count += 1
            # Construct the source and destination file paths
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_dir, file)

            # Copy the MP3 file to the destination directory
            shutil.copy2(src_file_path, dest_file_path)

if mp3_count > 0:
    print(f"{mp3_count} MP3 songs copied successfully.")
else:
    print("No MP3 songs found.")
