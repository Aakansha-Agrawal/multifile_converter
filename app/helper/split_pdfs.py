import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from .savefile import savefile_format

def splitpdf(path, save_file, frompage, topage):
    print(path)
    m = int(frompage)
    n = int(topage)

    print(m,n)

    pdf = PdfFileReader(path)
    print(pdf.numPages)

    for page_num in range(pdf.numPages):
        
        # if ( (m!= None) and (n!= None)):
        while(m <= n):
            pdfwrite = PdfFileWriter()
            pdfwrite.addPage(pdf.getPage(m))
            
        # with open(os.path.join(out_path,'{0}_Page{1}.pdf'.format(file_base, page_num+1)), 'wb') as f:
            with open(os.path.join(save_file,'{0}_Page{1}.pdf'.format(savefile_format(path), m+1)), 'wb') as f:
                pdfwrite.write(f)
                f.close()

            m = m+1
    
    print("Conversion Completed")
