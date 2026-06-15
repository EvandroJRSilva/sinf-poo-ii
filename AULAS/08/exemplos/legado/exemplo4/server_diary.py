from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

banco_path = 'AULAS/09/exemplo4/diary.db'

def init_db():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, texto TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/entries', methods=['GET'])
def get_entries():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries ORDER BY data DESC')
    entries = [{'id': row[0], 'data': row[1], 'texto': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(entries)

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.json
    data['data'] = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (data, texto) VALUES (?, ?)', (data['data'], data['texto']))
    conn.commit()
    conn.close()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True, port=5003)