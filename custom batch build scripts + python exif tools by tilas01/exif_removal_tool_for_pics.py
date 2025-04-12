#!/usr/bin/env python3
#this script was made with the help of chatgpt and edited by tilas01 on github

import os
import sys
import shutil
import datetime
from PIL import Image

# Configuration
INPUT_DIR = "pics"      # Original images (serves as backup)
OUTPUT_DIR = "pics_out" # Processed images
LOG_FILENAME = "exif_removal.log"
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png")

def print_progress_bar(iteration, total, prefix="", suffix="", decimals=1, length=50, fill="█"):
    """
    Displays or updates a console progress bar.
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    # Use carriage return to update the line in place.
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')

def process_image(in_file_path, out_file_path):
    """
    Opens an image from in_file_path and re-saves it to out_file_path,
    stripping any extra metadata (specifically EXIF data).

    Returns:
        had_exif (bool): True if EXIF data was found (and omitted).
        exif_size (int): Number of bytes of the EXIF data (if found), otherwise 0.
    """
    had_exif = False
    exif_size = 0
    ext = os.path.splitext(in_file_path)[1].lower()

    try:
        with Image.open(in_file_path) as img:
            # Check for EXIF metadata.
            if "exif" in img.info:
                had_exif = True
                if isinstance(img.info["exif"], bytes):
                    exif_size = len(img.info["exif"])
            
            # Copy image and re-save without including metadata.
            new_img = img.copy()
            # Choose parameters based on extension.
            if ext in (".jpg", ".jpeg"):
                new_img.save(out_file_path, format="JPEG", quality=100, subsampling=0)
            elif ext == ".png":
                new_img.save(out_file_path, format="PNG", compress_level=0)
    except Exception as e:
        # Print error (on a new line so as not to disturb the progress bar).
        sys.stdout.write('\n')
        print(f"Error processing {in_file_path}: {e}")
        return False, 0

    return had_exif, exif_size

def main():
    # Banner message with verbose info.
    print("EXIF & Metadata Stripper")
    print("This utility strips EXIF/metadata from image files and outputs them to '{}'.".format(OUTPUT_DIR))
    print("The original images in '{}' will remain untouched as a backup.\n".format(INPUT_DIR))

    # Check if the input directory exists.
    if not os.path.isdir(INPUT_DIR):
        print(f"Directory '{INPUT_DIR}' not found.")
        return

    # Create the output directory if it doesn't exist.
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

    # Gather list of supported files from the input directory.
    file_list = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(SUPPORTED_EXTENSIONS)]
    total_files = len(file_list)

    if total_files == 0:
        print("No supported image files found in '{}'.".format(INPUT_DIR))
        return

    print(f"Processing {total_files} images (stripping metadata)...\n")

    # Prepare logging details.
    log_lines = []
    
    # Process each file with an in-place progress bar.
    for i, filename in enumerate(file_list, start=1):
        in_file_path = os.path.join(INPUT_DIR, filename)
        out_file_path = os.path.join(OUTPUT_DIR, filename)

        # Ensure the output directory for the file exists.
        out_file_dir = os.path.dirname(out_file_path)
        os.makedirs(out_file_dir, exist_ok=True)

        # Get file size before processing.
        try:
            size_before = os.path.getsize(in_file_path)
        except Exception as e:
            size_before = 0
            print(f"Could not get size for {filename}: {e}")

        # Process the image.
        had_exif, exif_size = process_image(in_file_path, out_file_path)

        # Get file size after processing.
        try:
            size_after = os.path.getsize(out_file_path)
        except Exception as e:
            size_after = 0
            print(f"Could not get size for processed file {filename}: {e}")

        # Build a detailed log message.
        if had_exif:
            msg = (f"{filename}: Removed {exif_size} bytes of EXIF data. "
                   f"Size before: {size_before} bytes, after: {size_after} bytes.")
        else:
            msg = (f"{filename}: No EXIF data found. "
                   f"Size before: {size_before} bytes, after: {size_after} bytes.")
        log_lines.append(msg)

        # Update progress bar.
        print_progress_bar(i, total_files, prefix="Progress:", suffix="Complete", length=50)

    # Write the log file.
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
