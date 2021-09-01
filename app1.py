import os
import requests
from flask import Flask, render_template, request
from predictor import check
from werkzeug.utils import secure_filename

 
author = 'ineuron'  
app = Flask(__name__)
#app.secret_key = 'secret'
#app.static_folder="images"
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index(): 
    return render_template('upload.html')

  
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    for file in request.files.getlist('file'): 

        #print(file) 

        filename = file.filename
        #filename =file.filename
        print(filename)
        dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(dest)  
        file.save(dest)   
    label = check(filename)
    print(label)
    return render_template('complete.html', predvalue=label)
 
 
if __name__ == "__main__": 
    app.run(port=4555, debug=True)