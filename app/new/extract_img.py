import fitz
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter import Tk
import os

root = Tk()
root.withdraw()

def extractimages(path, save_file):
    # pdf_file = askopenfilename()
    file = fitz.open(pdf_file)

    # extract image
    for pageNum, page in enumerate(file.pages(), start = 1):
        for imgNum, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            pix = fitz.Pixmap(file, xref)

            # From documentation : pix.n => bytes per pixel
            if pix.n > 4: # since this is no Gray or RGB

                #convert into RGB pixmap
                pix = fitz.Pixmap(fitz.csRGB, pix)            
            
            save_img = os.path.join(save_file, "image_{0}_{1}.png".format(pageNum, imgNum))
            pix.writePNG(f'image_{pageNum}_{imgNum}.png')
            # print(pic_file)

extractimages()


