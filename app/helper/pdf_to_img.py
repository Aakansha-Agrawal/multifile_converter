from pdf2image import convert_from_path 
import os  
from .savefile import savefile_format

def pdftoimage(path, save_file):
    pdf_file = path
    images = convert_from_path(pdf_file, poppler_path = r"C:\Users\aakan\Desktop\multifile_converter\poppler-0.68.0\bin") 

    #iterating enumerate in whole pdf
    for idx,page in enumerate(images):
        
    #   page.export('pdf_file', f="csv", compress=True)

        # page.save('image_page_'+ str(idx) +'.jpg', 'JPEG')
        savefile = os.path.join(save_file,"{0}_{1}.jpg".format(savefile_format(path),str(idx)))
        page.save(savefile, 'JPEG')