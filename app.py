from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact_page():
    return render_template('contacts.html')

@app.route('/all_books_static')
def books_page():
    return render_template('books.html')
