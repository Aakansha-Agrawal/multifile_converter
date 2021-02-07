from pdf2docx import parse
from tkinter import Tk
from tkinter.filedialog import askopenfilename,asksaveasfile,asksaveasfilename
import os

root = Tk()
root.withdraw()

# pdf_file = 'Unit-1 PPT.pdf'
file = askopenfilename()
fpath = os.path.basename(file)
file_base = fpath.replace('.pdf','')
print(fpath,file_base)

# docx_file = asksaveasfilename(initialfile="untitled.docx")
pdffile = "E:\\Converted_Files\\"
save_file = os.path.join(pdffile,"{0}.docx".format(file_base))

# convert pdf to docx
try:
    parse(file, save_file)

except:
    print("Images Found")
    pass