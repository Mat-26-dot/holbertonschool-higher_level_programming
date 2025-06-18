from flask import request, Flask, jsonify

app = Flask(__name__)

books = []

@app.route('/books', methods=['GET', 'POST'])
def books_endpoint():
    if request.method == 'POST':
        new_book = request.get_json()
        books.append(new_book)
        print(books)
        return jsonify({'message': 'Book added'}), 201
    else:
        return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=True)