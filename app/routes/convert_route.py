from app import app 
import os, pathlib, secrets, console
from flask import request, make_response, jsonify, redirect, render_template, session, send_from_directory, send_file
from werkzeug.utils import secure_filename
from .category_route import categories 

app.config['UPLOAD_FOLDER'] = 'E:\\Project_Files\\uploaded_files'
app.config['CONVERT_FOLDER'] = 'E:\\Project_Files\\converted_files'
ALLOWED_EXTENSIONS = {'.doc','.docx','.txt','.pdf','.png','.jpg','.jpeg'}
app.config['SECRET_KEY'] = 'super secret'
app.config['DEBUG'] = True

from app.converting_scripts import (imgtopdf,pdftoaudio,texttospeech, texttopdf, pdftotext)

@app.route("/uploadfile/<filetype>", methods=["POST","GET"])
def send_file(filetype):

    if request.method == "POST":
        if not session.get("count") is None:
            print("Session exist")

        else:
            session['count'] = secrets.token_urlsafe(6)
            session['count'] = filetype + '___' + session['count']

            filesize = request.cookies.get("filesize")
            file = request.files["file"]
            # print(f"Filesize: {filesize}",file.filename)

            res = make_response(jsonify({"message" : f"{file.filename} uploaded"}), 200)

            file_ext = pathlib.Path(file.filename).suffix

            if file_ext in ALLOWED_EXTENSIONS :
                
            #--------------------------- saving file to folder ------------------------------ #   
                upload_path = os.path.join(app.config['UPLOAD_FOLDER'],session['count'])
                convert_path = os.path.join(app.config['CONVERT_FOLDER'],session['count'])
                os.makedirs(upload_path)
                os.makedirs(convert_path)

                if os.path.isdir(upload_path) and os.path.isdir(convert_path):
                    file.save(os.path.join(upload_path, file.filename))
                    print("File Uploaded")
                    
                    # ---------------------- calling function to convert ---------------------- #
                    f = os.path.abspath(file.filename)
                    # print(f)

                    if filetype == 'image_to_pdf':
                        imgtopdf(f, convert_path)
                    elif filetype == 'pdf_to_audio':
                        pdftoaudio(f, convert_path)
                    elif filetype == 'text_to_audio':
                        texttospeech(file.filename, convert_path)
                    elif filetype == 'text_to_pdf':
                        texttopdf(f, convert_path)
                    elif filetype == 'pdf_to_text':
                        pdftotext(f, convert_path)
                    else:
                        print("not valid")

                else:
                    print('not found')
            
            else:
                print("extension not allowed")
            
            return res
            # , send_from_directory(directory=convert_path, filename=filetype, as_attachment=True)


    catg = None
    if filetype in categories:
        catg = categories[filetype]
        
    return render_template("convert.html",filetype=filetype, catg=catg) 

@app.route('/uploadfile/')
def get_file():
    # try:
    #     return send_file("/E:/Project_Files/uploaded_files/untitled.docx", as_attachment=True) 
    #    #I also tried flask.send_file and send_static_file
    # except:
    #     return("Generic error message")
    return send_file("/E:/Project_Files/uploaded_files/untitled.docx") 
    # return send_from_directory("/E:/Project_Files/uploaded_files/", filename='untitled.docx', as_attachment=True)



@app.route('/clear_count')
def clear_count():
    session.pop('count', None)
    print("session cleared")
    return 'Counter Cleared'