from PyPDF2 import PdfFileMerger
import os
# from tkinter.filedialog import asksaveasfile,asksaveasfilename,askdirectory
# from tkinter import Tk

# root = Tk()
# root.withdraw()

def mergepdf(path, save_file, upload_path):
    # files = askdirectory()
    merger = PdfFileMerger()

    for i in os.listdir(upload_path):  
        if i.endswith('.pdf'):
            print(i)
            merger.append(i)
    #         print(merger)

    # savefile = asksaveasfilename(initialfile="untitled.pdf")
    savefile = os.path.join(save_file,"merged.pdf")
    merger.write(savefile)

    merger.close()
