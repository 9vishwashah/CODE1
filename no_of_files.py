from importlib.resources import path
import os
path=input("Paste the path from your pc:\n")
file_count=0
dir_count=0
for root, dirs, files in os.walk(path):
    print('Looking in:',root)
    for directories in dirs:
        dir_count+=1
    for files in files:
        file_count+=1
print("Number of Files",file_count)
print("Numberr of Directories",dir_count)
print("Total:",dir_count+file_count)
