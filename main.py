# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:36:12 2019

@author: vaishnov
"""
'''
import os
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template,send_file
from integ import process_data
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']

		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
            
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)
      

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    #path = "E:\\ML\\elction roll\\Voters list_new.csv"
    path = out
    return send_file(path, as_attachment=True)



if __name__ == "__main__":
    app.run()

'''

from flask import Flask, make_response, request
from app import app
from integ import process_data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def file_summer_page():
    if request.method == "POST":
        input_file = request.files["input_file"]
        input_data = input_file.stream.read().decode("utf-8")
        output_data = process_data(input_data)
        response = make_response(output_data)
        response.headers["Content-Disposition"] = "attachment; filename=result.csv"
        return response

    return '''
        <html>
            <body>
                <p>Select the file you want to sum up:</p>
                <form method="post" action="." enctype="multipart/form-data">
                    <p><input type="file" name="input_file" /></p>
                    <p><input type="submit" value="Process the file" /></p>
                </form>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run()   