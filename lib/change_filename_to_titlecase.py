#import os.path

# Get a list of all the file paths that ends with .txt from in specified directory

#fileList = glob.glob('C:\Users\Owner\Desktop\Test folder')

# Iterate over the list of filepaths & remove each file.

#for file in fileList:
#    try:
#        os.rename(file, file.title())
#    except:
#        print("Error while modifying filename : ", file)



import pathlib
from pathlib import Path

# create variable, assigned the path
p = pathlib.Path(r"C:\Users\Owner\Desktop\Test folder\ABC Test.txt")

# print to check it worked. Unnecessary. 

filename_without_extension = p.stem
filename_extension = p.suffix
#print(p.stem)
#print(p.suffix)

# Create variable with value to replace original filename
new_file_name = f"{filename_without_extension.title()}"

# Rename original filename with new filename, + preserved suffix / filetype / extension
p.rename(Path(p.parent, new_file_name + filename_extension))

print(p.stem)




# create new string from substrings of original, inserting a gap
#new_stem = p.stem[:3] + " " + p.stem[3:]

# run the renaming 
#p.rename(Path(p.parent, new_stem + filename_extension))