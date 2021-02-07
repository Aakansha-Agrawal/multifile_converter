import PyPDF2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfile, askopenfilename,asksaveasfilename,asksaveasfile

root = Tk()
root.withdraw()

# pdffileobj=open('Unit.pdf','rb')
# pdffileobj = open(askopenfile(),"r")
pdffileobjj = askopenfilename()
pdffileobj = open(pdffileobjj, 'r')
print(pdffileobj)

file_open = getattr(pdffileobj,'name')
# print(file_open)

pdfreader=PyPDF2.PdfFileReader(file_open)
x=pdfreader.numPages
path = 'E:\\Project_Files\\'

# file1=open(r"C:\Users\aakan\Desktop\pp\myprojectdata\New\\file.txt","w",encoding='utf-8')
# file1 = asksaveasfile(initialfile="untitled.txt", mode="w", defaultextension=".txt")

file1 = os.path.join(path,"unnn.txt")
open_file = open(file1,'w')
print(file1)

for i in range (0,x):
    pageobj=pdfreader.getPage(i)
    text=pageobj.extractText()
    open_file.writelines(text)
    # print(text)

    open_file.write("\n\n".join(text)) 
