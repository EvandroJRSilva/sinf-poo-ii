from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

banco_path = 'AULAS/09/exemplo5/books.db'

def init_db():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, lido BOOLEAN)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'id': row[0], 'titulo': row[1], 'autor': row[2], 'lido': bool(row[3])} for row in cursor.fetchall()]
    conn.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (titulo, autor, lido) VALUES (?, ?, ?)', 
                   (data['titulo'], data['autor'], False))
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': book_id, 'titulo': data['titulo'], 'autor': data['autor'], 'lido': False}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET lido = ? WHERE id = ?', (data['lido'], book_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Livro atualizado'})

if __name__ == '__main__':
    app.run(debug=True, port=5004)