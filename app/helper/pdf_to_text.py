import PyPDF2
import os
from .savefile import savefile_format

def pdftotext(path, save_file):
    # pdffileobj = open(path,'rb')
    path_s = path.replace("/","\\")
    pdffileobj = path_s
    print(pdffileobj,path)
 
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages

    file1 = os.path.join(save_file,"{0}.txt".format(savefile_format(path)))
    open_file = open(file1,"w")
    # print(file1)

    for i in range (0,x):
        pageobj=pdfreader.getPage(i)
        text=pageobj.extractText()
        open_file.writelines(text)
        # print(text)

        open_file.write("\n\n".join(text)) 
