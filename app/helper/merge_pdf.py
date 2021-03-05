from PyPDF2 import PdfFileMerger
import os
from tkinter.filedialog import asksaveasfile,asksaveasfilename,askdirectory
# from tkinter import Tk

# root = Tk()
# root.withdraw()

def mergepdf(save_file, filepath):

    merger = PdfFileMerger()

    for i in os.listdir(filepath):  
        print(i)
        if i.endswith('.pdf'):
            absfile = os.path.join(filepath, i)
            print(i)
            merger.append(absfile)
    #         print(merger)

    # savefile = asksaveasfilename(initialfile="untitled.pdf")
    savefile = os.path.join(save_file,"merged.pdf")
    merger.write(savefile)
    print("Conversion Completed")

    merger.close()


