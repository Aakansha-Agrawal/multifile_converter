import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image

root = Tk()
root.withdraw()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = askopenfilename(initialdir = "/",title = "Open",filetypes = (("Image files",".png",".jpg"),("All Files","*.*")))
value = Image.open(image)
# value = Image.open('pic.jpg')
text = pytesseract.image_to_string(value)
# pdf = pt.image_to_pdf_or_hocr(value,config='')
# data = pt.image_to_data(value,config='')
print(text)