from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk
import os

root = Tk()
root.withdraw()

def imgtopdf(path):
    # path = askopenfilename()
    path_s = path.replace("\","\\")

    save_file = 'E:\\Project_Files\\converted_files'
    print(path_s)
    file_name = os.path.basename(path_s)
    get_file = os.path.splitext(file_name)
    file_ext = get_file[1]
    file_base = file_name.replace(get_file[1], '')
    pdf = Image.open(path_s)

    # file = asksaveasfilename(initialfile="untitled.pdf")
    file = os.path.join(save_file, "{0}.pdf".format(file_base))
    pdf.save(file)

path = askopenfilename()
imgtopdf(path)
# save_file = 'E:\\Project_Files\\converted_files'
