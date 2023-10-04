import os

def scan_directory(directory):
    file_list = []
    for filename in os.listdir(directory):
        file_list.append(filename)
    return file_list




