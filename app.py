from flask import Flask, render_template, request, jsonify, Blueprint
from database.database import create_tables

from routes.booksRoutes import book_view
from routes.blogRoutes import blog_view
from routes.userRoute import user_view
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

# @app.route("/blog")
# def blog():
#     return jsonify(userController.get_All())


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method =='POST':
        f = request.files['file']
        if f.filename == '':
            return 'No selected file'
        if f:
            f.save('./biblio/f/tmp/'+ f.filename)
            return render_template('index.html')
        
app.register_blueprint(book_view)
app.register_blueprint(blog_view)
app.register_blueprint(user_view)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)