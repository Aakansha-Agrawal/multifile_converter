import pikepdf
import os
from .savefile import savefile_format

def unlock_pdf(path, save_file, filepass):
    mypdf = pikepdf.open(path, filepass)

    filesave = os.path.join(save_file, "{0}.pdf".format(savefile_format(path)))
    mypdf.save(filesave)
