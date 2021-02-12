import fitz
import os
from .savefile import savefile_format

def extractimages(path, save_file):
    file = fitz.open(path)

    # extract image
    for pageNum, page in enumerate(file.pages(), start = 1):
        for imgNum, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            pix = fitz.Pixmap(file, xref)

            # From documentation : pix.n => bytes per pixel
            if pix.n > 4: # since this is no Gray or RGB

                #convert into RGB pixmap
                pix = fitz.Pixmap(fitz.csRGB, pix)            
            
            pix.writePNG(save_file + '/' + str(savefile_format(path)) + '_' + str(pageNum) + '_' + str(imgNum) + '.png')


