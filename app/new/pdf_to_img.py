from pdf2image import convert_from_path 
from tkinter.filedialog import askopenfilename,askdirectory
import os  
from tkinter import Tk
  
root = Tk()
root.withdraw()

# Store Pdf with convert_from_path function 
pdf_file = askopenfilename()
images = convert_from_path(pdf_file, poppler_path = r"C:\Program Files\poppler-0.68.0\bin") 

# dir_path = askdirectory()
# files = dir_path.replace('/', '\\')

#iterating enumerate in whole pdf
for idx,page in enumerate(images):
    
#   page.export('pdf_file', f="csv", compress=True)

    page.save('image_page_'+ str(idx) +'.jpg', 'JPEG')
