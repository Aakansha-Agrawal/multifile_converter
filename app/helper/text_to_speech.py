import pyttsx3 
import os
from .savefile import savefile_format

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