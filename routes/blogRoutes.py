from flask import Blueprint, render_template, send_file, request, redirect
from controller.blogController import PostController
from controller.commentController import Comments
from database.database import get_db
from AI.parser import Parser
from AI.model import IaModel

blog_view = Blueprint('blog_routes', __name__, template_folder='/templates')
db = get_db()
postController = PostController(db)
commentesController = Comments(db)

text = ''
with open('./AI/result.txt', 'r') as fichier:
        text = fichier.readlines()

vocabulaire =  text[0].split(' ')
parser = Parser(vocabulaire)
iaModel = IaModel()

@blog_view.route('/blogs/')
def home():
    blogs = postController.get_All()
    print(blogs)
    return render_template('blog.html', blogs = blogs)

@blog_view.route('/blogs/create/', methods =['POST'])
def create():
    data = request.form
    print(data)
    id = data.get('id')
    title = data.get('title')
    content = data.get('content')
    classename = ''
    print(content)
    if content:
        data = parser.tokenizer(content)
        res = parser.parser(data)
        predres = iaModel.predict([res])
        if predres[0]== 'technologie':
             classename = 'technologie'
        if predres[0]== 'politique':
             classename = 'politique'
        if predres[0]== 'autre':
             classename = 'autre'
        resp = postController.create(id, title,content, classename)
        if resp:
            return redirect('/blogs/')
    return redirect('/blogs/')
            
@blog_view.route('/blogs/create/', methods =['GET'])
def createIndex():
    return render_template('createPost.html')

@blog_view.route('/blogs/<id>', methods = ['GET']) 
def show(id):
    post = postController.get_by_id(id)
    comment = commentesController.get_All_by_postId(id)
    return render_template('post.html',posts = post, comments = comment)

@blog_view.route('/blogs/<id>' , methods = ['POST']) 
def showCreate(id):
    data = request.form
    content = data.get('content')
    commentesController.create(int(1),id ,content)
    post = postController.get_by_id(id)
    comment = commentesController.get_All_by_postId(id)
    return render_template('post.html',posts = post, comments = comment)
   
@blog_view.route('/blogs/classe/<classename>', methods =['GET'])
def findClasse(classename):
    blogs = postController.get_by_classe(classename)
    return render_template('blog.html', blogs = blogs)