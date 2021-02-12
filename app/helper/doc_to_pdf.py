from docx2pdf import convert 
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Tk
import os

root = Tk()
root.withdraw()


def doctopdf():
    file = askopenfilename()
    fpaths = os.path.basename(file)
    file_base = fpaths.replace('.docx','')
    # file_ext = os.path.splitext(file)
    print(fpaths,file_base)

    fpath = asksaveasfilename(initialfile = 'Untitled.pdf')
    
    convert(file, fpath)

doctopdf()
