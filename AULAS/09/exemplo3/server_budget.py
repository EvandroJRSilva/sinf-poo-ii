from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

banco_path = 'AULAS/09/exemplo3/budget.db'

def init_db():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT, valor REAL, data TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    expenses = [{'id': row[0], 'descricao': row[1], 'valor': row[2], 'data': row[3]} for row in cursor.fetchall()]
    total = sum(exp['valor'] for exp in expenses)
    conn.close()
    return jsonify({'expenses': expenses, 'total': total})

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    data['data'] = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (descricao, valor, data) VALUES (?, ?, ?)', 
                   (data['descricao'], data['valor'], data['data']))
    conn.commit()
    conn.close()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True, port=5002)