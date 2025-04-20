#this script was made with the help of chatgpt and edited by tilas01 on github
#this script is untested by me - as all scripts and the license states: use at your own risk!
#no issues have been submitted related to the above - please submit one if found
#!/usr/bin/env python3

import os
import sys
import shutil
import datetime
from PIL import Image

# Configuration
INPUT_DIR = "pics"
OUTPUT_DIR = "pics_out"
LOG_FILENAME = "exif_removal.log"
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png")

# Compression settings
JPEG_QUALITY = 85  # Adjust to control output size. Lower means more compression.
PNG_COMPRESSION_LEVEL = 9  # 0 = none, 9 = max compression

def print_progress_bar(iteration, total, prefix="", suffix="", decimals=1, length=50, fill="█"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')

def process_image(in_file_path, out_file_path):
    had_exif = False
    exif_size = 0
    ext = os.path.splitext(in_file_path)[1].lower()

    try:
        with Image.open(in_file_path) as img:
            if "exif" in img.info:
                had_exif = True
                if isinstance(img.info["exif"], bytes):
                    exif_size = len(img.info["exif"])

            new_img = img.copy()

            if ext in (".jpg", ".jpeg"):
                new_img.save(out_file_path, format="JPEG", quality=JPEG_QUALITY, optimize=True)
            elif ext == ".png":
                new_img.save(out_file_path, format="PNG", compress_level=PNG_COMPRESSION_LEVEL, optimize=True)

    except Exception as e:
        sys.stdout.write('\n')
        print(f"Error processing {in_file_path}: {e}")
        return False, 0

    return had_exif, exif_size

def get_all_image_files(base_dir):
    image_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, base_dir)
                image_files.append((full_path, relative_path))
    return image_files

def main():
    print("EXIF & Metadata Stripper (Recursive with Compression)")
    print(f"Input: '{INPUT_DIR}', Output: '{OUTPUT_DIR}'\n")

    if not os.path.isdir(INPUT_DIR):
        print(f"Directory '{INPUT_DIR}' not found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    image_files = get_all_image_files(INPUT_DIR)
    total_files = len(image_files)

    if total_files == 0:
        print(f"No supported image files found in '{INPUT_DIR}'.")
        return

    print(f"Processing {total_files} images...\n")
    log_lines = []

    for i, (in_file_path, relative_path) in enumerate(image_files, start=1):
        out_file_path = os.path.join(OUTPUT_DIR, relative_path)
        os.makedirs(os.path.dirname(out_file_path), exist_ok=True)

        try:
            size_before = os.path.getsize(in_file_path)
        except Exception as e:
            size_before = 0
            print(f"Could not get size for {in_file_path}: {e}")

        had_exif, exif_size = process_image(in_file_path, out_file_path)

        try:
            size_after = os.path.getsize(out_file_path)
        except Exception as e:
            size_after = 0
            print(f"Could not get size for processed file {relative_path}: {e}")

        if had_exif:
            msg = (f"{relative_path}: Removed {exif_size} bytes of EXIF. "
                   f"Before: {size_before}, After: {size_after}")
        else:
            msg = (f"{relative_path}: No EXIF found. "
                   f"Before: {size_before}, After: {size_after}")
        log_lines.append(msg)

        print_progress_bar(i, total_files, prefix="Progress:", suffix="Complete", length=50)

    try:
        with open(LOG_FILENAME, "w") as log_file:
            header = ("EXIF/Metadata Stripper Log - {}\n"
                      "Processed {} images from '{}' to '{}'\n"
                      "--------------------------------------------------\n").format(
                          datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          total_files, INPUT_DIR, OUTPUT_DIR)
            log_file.write(header)
            for line in log_lines:
                log_file.write(line + "\n")
        print(f"\nLog written to {LOG_FILENAME}")
    except Exception as e:
        print(f"Error writing log file: {e}")

if __name__ == '__main__':
    main()
