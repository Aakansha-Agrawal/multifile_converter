import PyPDF2
from gtts import gTTS
import os
from .savefile import savefile_format

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