# This my main python script for the Book Manager application

from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# Initializing the Flask application
app = Flask(__name__)

# Configuring the Data Base and initializing it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Defining the Book model for my sql_database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(100), default = 'unread')

    def __repr__(self):
        return f"Book('{self.title}', '{self.genre}')"


# Defining the first route 
@app.route('/', methods = ['GET','POST'])
def homepage():
    if request.method == 'POST':
        book_title = request.form.get('book')
        book_genre = request.form.get('genre')
        book_status = request.form.get('status')
        
        try:
            new_book = Book(title = book_title, genre =book_genre, status = book_status)
            db.session.add(new_book)
            db.session.commit()
        except:
            return 'There was an Issue with your submit to the database, please try it again'
    books = Book.query.all()
    return render_template('index.html', books = books)



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.status = request.form.get('status')
        try:
            db.session.commit()
            return redirect(url_for('homepage'))
        except:
            return 'There was an issue updating the book status'
    return render_template('update.html', book = book)



@app.route('/delete/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    try:
        db.session.delete(book)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue on trying to delete this data'


if __name__ == '__main__':
    # Assuring that the tables of the SQL alchemy querrys are created after the script is launched
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=3000)



