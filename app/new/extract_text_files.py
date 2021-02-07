import PyPDF2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfile,asksaveasfilename,asksaveasfile

root = Tk()
root.withdraw()

# pdffileobj=open('Unit.pdf','rb')
pdffileobj = askopenfile()
print(pdffileobj)

file_open = getattr(pdffileobj,'name')
# print(file_open)

pdfreader=PyPDF2.PdfFileReader(file_open)
x=pdfreader.numPages

for i in range (0,x):
    pageobj=pdfreader.getPage(i)
    text=pageobj.extractText()
    file1 = open(f'file_{i+1}.txt','w')
    file1.writelines(text)
    # print(file1)

file1.close()