"""
Author:      Vera Neroni
Date Created:     05/17/2023

Edited:
        - 11/25/25 - simplified test version for debugging


"""

import os
from pathlib import Path
import time

# request path for folder, which contains files to print
target_folder = input("Enter folder path: ")

#list all files in chosen folder
list_files = os.listdir(target_folder)

#make the list of files into a list of paths
list_paths = [os.path.join(str(target_folder), file) for file in list_files]

#create function: this function prints everything in the folder using the paths list
def print_all():
    for item in list_paths:
        os.startfile(item, "print")
        time.sleep(5)
    print("Printing job complete!")

#run the print function
print_all()
