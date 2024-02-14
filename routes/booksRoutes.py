from flask import Blueprint, render_template, jsonify, send_file, request, redirect
from controller.bookController import BookController
from AI.parser import Parser
from AI.model import IaModel
from PyPDF2 import PdfReader
import shutil

book_view = Blueprint('book_routes', __name__, template_folder='/templates')
bookController = BookController('./biblio/f/')


text = ''
with open('./AI/result.txt', 'r') as fichier:
        text = fichier.readlines()

vocabulaire =  text[0].split(' ')
parser = Parser(vocabulaire)
iaModel = IaModel()



# @book_view.route('/books/', defaults={'id': None})
@book_view.route('/books/')
def home():
    booksulrs = bookController.get_all()
    return render_template('books.html', books = booksulrs)

@book_view.route('/books/<classe>')
def classe(classe):
    booksulrs = bookController.get_by_classe(classe)
    return render_template('books.html', books = booksulrs)

@book_view.route('/books/read/<classe>/<name>')
def get_pdf(classe, name):
    return send_file(bookController.PATH+classe+"/"+name, as_attachment=False)

@book_view.route('/books/create/', methods = ['POST'])
def createpost():
    f = request.files['file']
    f2 = f 
    if f.filename == '':
        return render_template('createbook.html')
    if f:
        fname = f.filename
        filePath = './biblio/tmp/'+ f.filename
        f.save(filePath)
        pdfdata = PdfReader(filePath)
        content = ''
        with open(filePath, 'rb') as fichier:
            pdf = PdfReader(fichier)
            for c in range(len(pdf.pages)):
                p = pdf.pages[c]
                content+= p.extract_text()
        data = parser.tokenizer(content)
        res = parser.parser(data)
        predres = iaModel.predict([res])
        if predres[0]== 'technologie':
            shutil.copy(filePath, './biblio/f/technologie/'+fname)
        if predres[0]== 'politique':
            shutil.copy(filePath, './biblio/f/politique/'+fname)
        if predres[0]== 'autre':
            shutil.copy(filePath, './biblio/f/autre/'+fname)
        return redirect('/books/', 302)

@book_view.route('/books/create/', methods = ['GET'])
def create():
    return render_template('createbook.html')