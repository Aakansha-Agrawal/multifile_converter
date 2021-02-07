# from camelot import read_pdf
import camelot
from tkinter import Tk
from tkinter.filedialog import askopenfilename,asksaveasfilename 
import os

root = Tk()
root.withdraw()

# PDF file to extract tables from
files = os.path.basename(askopenfilename())

#reading files
tables = camelot.read_pdf(files)

#saving files
file_name = asksaveasfilename(initialfile='untitled.csv')
tables[0].to_csv(file_name)

# # or export all in a zip
# tables.export('files', f="csv", compress=True)

# export to HTML
# tables.export(asksaveasfilename(initialfile='file.html'))