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

from app.helper import imgtopdf, pdftoaudio, texttospeech, texttopdf, pdftotext, pdftoimage, extractimages, extract_img_text, pdftodocx, protect, unlock_pdf, splitpdf, mergepdf, doctopdf

@app.route("/uploadfile/<filetype>", methods=["POST","GET"])
def send_file(filetype):

    if request.method == "POST":              
        if not session.get("count") is None:
            print("Session exist")

        else:
            session['count'] = secrets.token_urlsafe(6)
            session['count'] = filetype + '___' + session['count']

            filesize = request.cookies.get("filesize")
            # file = request.files["file"]
            # filepass = request.cookies.get("filepass")

            frompage = request.cookies.get("frompage")
            topage = request.cookies.get("topage")
            print(frompage, topage)

            res = make_response(jsonify({"message" : "file uploaded"}), 200)

            files = request.files.getlist('file')
            # print(file,files)
               
            #--------------------------- saving file to folder ------------------------------ # 
            # for file in files:

            if files :

                upload_path = os.path.join(app.config['UPLOAD_FOLDER'],session['count'])
                convert_path = os.path.join(app.config['CONVERT_FOLDER'],session['count'])

                os.makedirs(upload_path)
                os.makedirs(convert_path)

                if os.path.isdir(upload_path) and os.path.isdir(convert_path):
                    
                    for file in files:
                        file_ext = pathlib.Path(file.filename).suffix

                        if file_ext in ALLOWED_EXTENSIONS:

                            filename = secure_filename(file.filename)
                            file.save(os.path.join(upload_path, filename))
                            print("File Uploaded")
                        
                        # ---------------------- calling function to convert ---------------------- #
                    f = os.path.abspath(os.path.join(upload_path, file.filename))
                    filepath = os.path.abspath(upload_path)

                    if filetype == 'image_to_pdf':
                        imgtopdf(f, convert_path)
                    elif filetype == 'pdf_to_audio':
                        pdftoaudio(f, convert_path)
                    elif filetype == 'text_to_audio':
                        texttospeech(f, convert_path)
                    elif filetype == 'text_to_pdf':
                        texttopdf(f, convert_path)
                    elif filetype == 'pdf_to_text':
                        pdftotext(f, convert_path)
                    elif filetype == 'pdf_to_image':
                        pdftoimage(f, convert_path)
                    elif filetype == 'extract_images':
                        extractimages(f, convert_path)
                    elif filetype == 'extract_images_text':
                        extract_img_text(f, convert_path)
                    elif filetype == 'pdf_to_word':
                        pdftodocx(f, convert_path)
                    elif filetype == 'protect_pdf':
                        protect(f, convert_path, filepass)
                    elif filetype == 'unlock_pdf':
                        unlock_pdf(f, convert_path, filepass)
                    elif filetype == 'merge_pdf':
                        mergepdf(convert_path, filepath)    
                    elif filetype == 'split_pdf':
                        splitpdf(f, convert_path, frompage, topage)
                    elif filetype == 'word_to_pdf':
                        doctopdf(f, convert_path)
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