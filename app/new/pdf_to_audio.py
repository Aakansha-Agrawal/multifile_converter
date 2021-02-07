import PyPDF2
from gtts import gTTS
import os
from tkinter import Tk
from tkinter.filedialog import askopenfile,asksaveasfile,asksaveasfilename,askopenfilename

root = Tk()
root.withdraw()

# # pdffileobj=open('file.pdf','rb')
def pdftoaudio(save_file):
    pdffileobj = askopenfilename()
    print(pdffileobj)
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages

    file_name = os.path.basename(pdffileobj)
    remov = file_name.replace(".pdf","")

    # file1=open(r"C:\Users\aakan\Desktop\pp\myprojectdata\New\\file.txt","w",encoding='utf-8')
    file1 = os.path.join(save_file,"{0}.txt".format(remov))
    open_file = open(file1,"w")

    # print(file1,open_file,pdffileobj)
    attr_name = getattr(open_file,'name')

    for i in range (0,x):
        pageobj=pdfreader.getPage(i)
        text=pageobj.extractText()
        open_file.writelines(text)
        # print(text)

    open_file.close()

    # file2=open(os.path.basename(file1),'r')
    file2=open(file1,'r')
    # print(file2,opn_f)

    mytext=file2.read()

    language='en'

    audio=gTTS(text=mytext,lang=language,slow=False)

    audfile = asksaveasfilename(initialfile = "untitled.wav",defaultextension=".wav")
    audio.save(audfile)
    # os.system(audfile)
    print("Conversion is Completed")

save_file = 'E:\\Project_Files\\converted_files'
pdftoaudio(save_file)
