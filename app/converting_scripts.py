from PIL import Image
import os

def savefile_format(path):
    file_name = os.path.basename(path)
    file_ext = os.path.splitext(file_name)[1]
    file_base = file_name.replace(file_ext, '')
    return file_base

def imgtopdf(path, save_file):
    # print(path, save_file)
    path_s = path.replace("/","\\")
    pdf = Image.open(path)
    print(path_s,path)

    file = os.path.join(save_file, "{0}.pdf".format(savefile_format(path)))
    pdf.save(file)


import PyPDF2
from gtts import gTTS

def pdftoaudio(path, save_file):
    paths = path.replace("/","\\")
    pdffileobj = paths
    print(path, pdffileobj)
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages

    open_file = os.path.join(save_file, "{0}.txt".format(savefile_format(path)))
    file1 = open(os.path.basename(open_file), "w")
    # print(file1)

    for i in range (0,x):
        pageobj=pdfreader.getPage(i)
        text=pageobj.extractText()
        file1.writelines(text)
        print(text)

    file1.close()
    file2=open(os.path.basename(open_file), "r")
    mytext=file2.read()

    audio=gTTS(text=mytext,lang='en',slow=False)

    audfile = os.path.join(save_file, "{0}.wav".format(savefile_format(path)))
    audio.save(audfile)
    # os.system(audfile)
    print("Conversion is Completed")


def pdftotext(path, save_file):
    # pdffileobj = open(path,'rb')
    path_s = path.replace("/","\\")
    pdffileobj = path_s
    print(pdffileobj,path)
 
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages

    file1 = os.path.join(save_file,"{0}.txt".format(savefile_format(path)))
    open_file = open(file1,"w")
    # print(file1)

    for i in range (0,x):
        pageobj=pdfreader.getPage(i)
        text=pageobj.extractText()
        open_file.writelines(text)
        # print(text)

        open_file.write("\n\n".join(text)) 


import pyttsx3 
def texttospeech(path,save_file):
    engine = pyttsx3.init(driverName='sapi5')

    #reading file
    path_s = path.replace("/","\\")
    infile = path_s
    f = open(infile, 'r')
    theText = f.read()
    f.close()

    #saving file
    engine.save_to_file(theText,os.path.join(save_file,"{0}.wav".format(savefile_format(path))))
    engine.runAndWait()


from fpdf import FPDF
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
    save_file = os.path.join(save_file,"{0}.pdf".format(savefile_format(path)))
    pdf.output(save_file)
