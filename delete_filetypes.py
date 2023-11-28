import os
import glob

# Get a list of all the file paths that ends with .txt from in specified directory

fileList = glob.glob('G:/000 All Footage/DCIM/100GOPRO/zKite Thief 2022 Godney Gathering/*.THM')

# Iterate over the list of filepaths & remove each file.

for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)