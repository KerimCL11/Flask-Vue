from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def load_books():
    with open('books.json', 'r') as file:
        return json.load(file)

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    books = load_books()
    if request.method == 'POST':
        post_data = request.get_json()
        books.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        save_books(books)
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = books
    return jsonify(response_object)

@app.route('/books/<string:title>', methods=['DELETE'])
def delete_book(title):
    books = load_books()
    books = [book for book in books if book['title'] != title]
    save_books(books)
    return jsonify({'status': 'success', 'message': 'Book deleted'})

@app.route('/books/<string:title>', methods=['PUT'])
def update_book(title):
    books = load_books()
    post_data = request.get_json()
    for book in books:
        if book['title'] == title:
            book['author'] = post_data.get('author', book['author'])
            book['read'] = post_data.get('read', book['read'])
            break
    save_books(books)
    return jsonify({'status': 'success', 'message': 'Book updated'})


if __name__ == '__main__':
    app.run()
