from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(120), nullable = False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id, self.book_name}"

@app.route('/')
def index():
    return "Hello!"

@app.route('/books')
def getBooks():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author}
        output.append(book_data)
    return {'books': output}

@app.route('/book/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.book_name, "author": book.author}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_title=request.json['book_name'], author=request.json['author'])
    db.session.add(book)
    db.session.commit()
    return{'id': book.id}