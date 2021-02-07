import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Tk

root = Tk()
root.withdraw()

pdffile = os.path.basename(askopenfilename(initialdir='/'))
file_base = pdffile.replace('.pdf','')

pathdir = askdirectory()
files = pathdir.replace('/', '\\')
# print(os.path.dirname(pathdir),os.path.dirname(files))

pdf = PdfFileReader(pdffile)

for page_num in range(pdf.numPages):
    pdfwrite = PdfFileWriter()
    pdfwrite.addPage(pdf.getPage(page_num))

    # with open(os.path.join(out_path,'{0}_Page{1}.pdf'.format(file_base, page_num+1)), 'wb') as f:
    with open(os.path.join(files,'{0}_Page{1}.pdf'.format(file_base, page_num+1)), 'wb') as f:
        pdfwrite.write(f)
        f.close()