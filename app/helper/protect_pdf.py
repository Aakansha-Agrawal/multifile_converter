from PyPDF2 import PdfFileWriter, PdfFileReader 
import os
from .savefile import savefile_format

def protect(path,save_file,filepass):
    out = PdfFileWriter() 

    file = PdfFileReader(path) 

    num = file.numPages 

    for idx in range(num): 	
        page = file.getPage(idx) 
        out.addPage(page) 

    password = filepass

    out.encrypt(password) 


    with open(os.path.join(save_file,"{0}.pdf".format(savefile_format(path))), "wb") as f: 
        out.write(f)
