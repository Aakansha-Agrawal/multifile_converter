import pyttsx3 
from tkinter import Tk
from tkinter.filedialog import askopenfilename,asksaveasfilename,askopenfile
import os

root = Tk()
root.withdraw()

# initialisation 
def texttospeech():
    engine = pyttsx3.init(driverName='sapi5')

    #reading file
    infile = askopenfilename()
    print(infile)

    f = open(infile, 'r')
    theText = f.read()
    f.close()

    #saving file
    file_name = os.path.basename(infile)
    remov = file_name.replace(".txt","")

    engine.save_to_file(theText,os.path.join('E:\\Project_Files',"{0}.wav".format(file_name)))
    engine.runAndWait() 

texttospeech()