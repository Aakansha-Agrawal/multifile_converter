import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from .savefile import savefile_format

def splitpdf(path, save_file, frompage, topage):
    # m = int(input("from : "))
    # n = int(input("to : "))
    m = frompage
    n = topage

    # root = Tk()
    # root.withdraw()

    # pdffile = askopenfilename()
    # pdffile = path
    # file_base = pdffile.replace('.pdf','')

    # pathdir = askdirectory()
    # files = pathdir.replace('/', '\\')
    # print(os.path.dirname(pathdir),os.path.dirname(files))

    pdf = PdfFileReader(path)
    print(pdf.numPages)


    for page_num in range(pdf.numPages):
        # print(page_num)
        while(m <= n):
            print(m,n)
            pdfwrite = PdfFileWriter()
            pdfwrite.addPage(pdf.getPage(m))
            
        # with open(os.path.join(out_path,'{0}_Page{1}.pdf'.format(file_base, page_num+1)), 'wb') as f:
            with open(os.path.join(save_file,'{0}_Page{1}.pdf'.format(savefile_format(path), m+1)), 'wb') as f:
                pdfwrite.write(f)
                f.close()

            m = m+1