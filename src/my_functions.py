from email import contentmanager
from importlib.resources import contents
from logging import RootLogger


import os
from re import sub

# walk the folder structure from root
def process_md_files(rootDir):
    
    print('Walking: ' + os.path.abspath(rootDir))

    for dirpath, dirnames, files in os.walk(rootDir):
        for item in files:
            if item.endswith(".md"):
                fileNamePath = str(os.path.join(dirpath,item))
                fullFileNamePath = os.path.abspath(fileNamePath)
                process_md_file(fullFileNamePath)

# operate on a single file
def process_md_file(filepath):
    print(filepath)

    file = open(filepath, "r")
    
    for line in file.readlines():
        ll = line.lower()
        is_in_line = ("no-content" in ll)

        if is_in_line:
            print(ll)
    
    file.close()
