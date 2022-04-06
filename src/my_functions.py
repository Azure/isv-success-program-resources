from pathlib import Path
from importlib.resources import contents
from logging import RootLogger
import os
from re import sub

# walk the folder structure from root
def process_md_files(root_dir):
    
    print('Walking: ' + os.path.abspath(root_dir))

    for path in Path(root_dir).rglob("*.md"):
        abs_file_path = os.path.abspath(path)
        list_significant_lines_in_md_file(abs_file_path)
        # lowercase_the_file_name(abs_file_path)

# look into a single file
def list_significant_lines_in_md_file(filepath):

    print(filepath)

    file = open(filepath, "r")
    
    line_count = 0
    for line in file.readlines():
        line_count += 1
        if ("no-" in line.lower()):
            print("Line: " + str(line_count) + " " + line, end="")
    
    file.close()

# ensure the file name is lowercase
def lowercase_the_file_name(filepath):
    os.rename(filepath, filepath.lower())