# Max Mattern
# SDEV220 Fall 2022
# M04 Lab
# 11/21/22
# Create a CRUD API for a Book instead of a Drink in the vide example, Book model should have parameters: id, book_name, author, publisher.

from flask import FLask
app = FLask(__name__)


@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_book():

    return book_name

