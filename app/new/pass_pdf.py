from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import *
from tkinter import messagebox
# import tkMessageBox
# import tkinter

root = Tk()
root.withdraw()

# def enter_password():
root.geometry('300x200')
root.title("Your Password")
#disable maximize button
root.resizable(0,0)

passwrd_1 = StringVar()
passwrd_2 = StringVar()

def enter(pdf):
    win_frame = Frame(root,bg="white",height=600) 
    win_frame.pack()

    title_label = Label(win_frame,bg="white",text="Enter Your Password",font=("Arial",17))
    title_label.grid(row=1,pady=10)

    pass_entry = Entry(win_frame,width=45,bd='4',textvar=passwrd_1)
    pass_entry.insert(0, 'Enter Password')
    pass_entry.grid(row=2,pady=10,ipady=5)

    pass_entry2 = Entry(win_frame,width=45,bd='4',textvar=passwrd_2)
    pass_entry2.insert(0, 'Confirm Password')
    pass_entry2.grid(row=3,ipady=5)

    Button(win_frame, text='Submit',width=25,bg='brown',fg='white',command=get_data).grid(row=4,pady=10,ipady=3)
    # win_frame.destroy()
    root.mainloop()
    return pdf

def get_data():
    get_passwrd_1 = passwrd_1.get()
    get_passwrd_2 = passwrd_2.get()

    if(get_passwrd_1 == get_passwrd_2):
        print("same")
                
        #get password
        passw = get_passwrd_1

        #encrypt password
        pdfwriter.encrypt(passw)

        root.destroy()

        #for next window
        tk = Tk()
        tk.withdraw()

        #writing & saving file
        save_file = asksaveasfilename(initialfile="Protected.pdf",defaultextension=".pdf")
        print(save_file)
        with open(save_file,'wb') as f:
            pdfwriter.write(f)
            f.close()
    else:
        print('not')
        #dialog box
        messagebox.showwarning("Check Password","Please Enter Same Password")

    
pdfwriter = PdfFileWriter()

pdf = PdfFileReader(askopenfilename())

if(pdf == " "):
    print("empty")
else:
    root.deiconify()
    #reading and adding pages
    for page_num in range(pdf.numPages):
        pdfwriter.addPage(pdf.getPage(page_num))
        # print(page_num)

    #calling function and passing pdf file
    enter(pdf)

