from fpdf import FPDF
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def convert_file(file, file_base):

    pdf = FPDF()
    pdf.add_page()

    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial",size=10)  #text title
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=10)  #paragraph text
            pdf.multi_cell(w=0,h=10,txt=text,align="L")

    # pdffile = asksaveasfilename(initialfile="untitled.pdf")
    
    pdffile = "E:\\Project_Files"
    save_file = os.path.join(pdffile,"{0}.pdf".format(file_base))
    pdf.output(save_file)

root = Tk()
root.withdraw()

files = askopenfilename()
file = open(files,'r')
# file = open('C:\\Users\\aakan\\Desktop\\Pdf Project\\Project\\file.txt','r')
atrr = getattr(file,'name')
fpath = os.path.basename(atrr)
file_base = fpath.replace('.txt','')
print(file,atrr)

convert_file(file, file_base)
