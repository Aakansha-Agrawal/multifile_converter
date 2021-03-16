from docx2pdf import convert 
# from tkinter.filedialog import askopenfilename,asksaveasfilename
# from tkinter import Tk
from .savefile import savefile_format
import os

# root = Tk()
# root.withdraw()


def doctopdf(path, save_file):
    file = path
    # file = askopenfilename()
    # fpaths = os.path.basename(file)
    # file_base = fpaths.replace('.docx','')
    # # file_ext = os.path.splitext(file)
    # print(fpaths,file_base)

    # fpath = asksaveasfilename(initialfile = 'Untitled.pdf')
    fpath = os.path.join(save_file, "{0}.pdf".format(savefile_format(path)))
    
    convert(file, fpath)

# doctopdf()
