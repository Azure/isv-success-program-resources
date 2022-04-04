from email import contentmanager
from importlib.resources import contents
from logging import RootLogger
import os
from re import sub

# walk the folder structure from root
def process_md_files(root_dir):
    
    print('Walking: ' + os.path.abspath(root_dir))

    for dirpath, dirnames, files in os.walk(root_dir):
        for item in files:
            if item.endswith(".md"):
                fileNamePath = str(os.path.join(dirpath,item))
                fullFileNamePath = os.path.abspath(fileNamePath)
                process_md_file(fullFileNamePath)

# operate on a single file
def process_md_file(filepath):

    print(filepath)
    file = open(filepath, "r")
    
    line_count = 0
    for line in file.readlines():
        line_count += 1
        if ("no-" in line.lower()):
            print("Line: " + str(line_count) + " " + line, end="")
    
    file.close()
