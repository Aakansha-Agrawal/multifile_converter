import fitz
import os
from .savefile import savefile_format

def extract_img_text(path, save_file):
    file = fitz.open(path)

    #extract text
    for pageNum, page in enumerate(file.pages(), start = 1):
        text = page.getText()

        file1 = os.path.join(save_file,"{0}_{1}.txt".format(savefile_format(path),pageNum))
        txt = open(file1,"w")
        # txt = open("file_{pageNum}.txt",'w')
        txt.writelines(text)
        txt.close()                                                                                     #run

    # # extract image
    for pageNum, page in enumerate(file.pages(), start = 1):
        for imgNum, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            pix = fitz.Pixmap(file, xref)

            # From documentation : pix.n => bytes per pixel
            if pix.n > 4: # since this is no Gray or RGB

                #convert into RGB pixmap
                pix = fitz.Pixmap(fitz.csRGB, pix)
            
            pix.writePNG(save_file + '/' + str(savefile_format(path)) + '_' + str(pageNum) + '_' + str(imgNum) + '.png')
