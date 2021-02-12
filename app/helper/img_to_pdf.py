from PIL import Image
import os
from .savefile import savefile_format

def imgtopdf(path, save_file):
    path_s = path.replace("/","\\")
    pdf = Image.open(path)
    print(path_s,path)

    file = os.path.join(save_file, "{0}.pdf".format(savefile_format(path)))
    pdf.save(file)

