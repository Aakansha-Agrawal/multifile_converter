import os

def savefile_format(path):
    file_name = os.path.basename(path)
    file_ext = os.path.splitext(file_name)[1]
    file_base = file_name.replace(file_ext, '')
    return file_base