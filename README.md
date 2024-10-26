# Flatten Directory Tool

This repository contains a Python script that flattens a directory structure by moving all files from subdirectories to the root directory. This can be useful when you need to consolidate files in a messy directory hierarchy or when you want to simplify file organization.

## Features
- **Efficient flattening**: The script traverses the entire directory tree and moves each file to the root directory while handling name conflicts gracefully by automatically renaming files if necessary.
- **Portable**: Written in Python, this tool can be run on various operating systems as long as Python is installed.

## Usage
1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using:
    ```bash
    python flatten_directory.py
    ```
4. The script will then start flattening the directory structure. You will see log messages indicating which files are being moved.

## Note
⚠️ **Be cautious when using this tool** as it will overwrite files with the same name in the root directory. Make sure to backup important data before running the script.

## Contributing
If you find any bugs or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

Let's keep our directories organized and clutter-free! 😊
