from fpdf import FPDF
import os
from .savefile import savefile_format

def texttopdf(path, save_file):
    file = open(path,'r')
    # file = getattr(file_open,'name')

    print(file)

    pdf = FPDF()
    pdf.add_page()

    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial",size=10)  #text title  
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=10)  #paragraph text
            pdf.multi_cell(w=0,h=10,txt=text,align="L")
    
    # pdffile = "E:\\Project_Files"
    savefile = os.path.join(save_file,"{0}.pdf".format(savefile_format(path)))
    pdf.output(savefile)