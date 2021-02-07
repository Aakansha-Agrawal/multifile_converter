from docx2pdf import convert 
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Tk
import os

root = Tk()
root.withdraw()

# not working properly

def doctopdf():
    file = askopenfilename()
    fpath = os.path.basename(file)
    file_base = fpath.replace('.docx','')
    # file_ext = os.path.splitext(file)
    print(fpath,file_base)

    # fpath = asksaveasfilename(initialfile = 'Untitled.pdf')
    pdffile = "E:\\Converted_Files\\"
    save_file = os.path.join(pdffile,"{0}.pdf".format(file_base))

    #coverts the pdf file to documnt and saving
    convert(file, save_file)

doctopdf()