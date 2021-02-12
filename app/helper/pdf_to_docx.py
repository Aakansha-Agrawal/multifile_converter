from pdf2docx import parse
import os
from .savefile import savefile_format

def pdftodocx(path, save_file):
    # file = askopenfilename()
    file = path
    
    save_file = os.path.join(save_file,"{0}.docx".format(savefile_format(path)))

    try:
        parse(file, save_file, )
        # parse(file, save_file, start=0, end=10)

    except:
        print("Images Found")
        pass