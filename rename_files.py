import os

def rename_files():
    # 1. extract files
    file_list = os.listdir(r"C:\Scripts\prank")
    #print file_list
    # 2. for each file, rename.
    saved_path = os.getcwd()
    os.chdir(r"C:\Scripts\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()