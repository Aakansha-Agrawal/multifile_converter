from PyPDF2 import PdfFileMerger
import os
from tkinter.filedialog import asksaveasfile,asksaveasfilename,askdirectory
from tkinter import Tk

root = Tk()
root.withdraw()

files = askdirectory()
merger = PdfFileMerger()

for i in os.listdir(files):  
    if i.endswith('.pdf'):
        print(i)
        merger.append(i)
#         print(merger)

savefile = asksaveasfilename(initialfile="untitled.pdf")
merger.write(savefile)

merger.close()
