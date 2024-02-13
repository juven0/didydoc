from flask import Flask, render_template, request, jsonify
from database.database import create_tables
from controller import userController

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    print(jsonify(userController.get_All()))
    return render_template('index.html')

@app.route("/blog")
def blog():
    return jsonify(userController.get_All())


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
    create_tables()
    app.run(debug=True)