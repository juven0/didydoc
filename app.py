from flask import Flask
from flask import render_template
from flask import request
import os
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method =='POST':
        f = request.files['file']
        if f.filename == '':
            return 'No selected file'
        if f:
            f.save('./biblio/f/tmp/'+ f.filename)
            return render_template('index.html')

if __name__ == "__main__":
    app.run()