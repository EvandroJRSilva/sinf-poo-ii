from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

banco_path = 'AULAS/09/exemplo2/contacts.db'

def init_db():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/contacts', methods=['GET'])
def get_contacts():
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = [{'id': row[0], 'name': row[1], 'email': row[2], 'phone': row[3]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', 
                   (data['name'], data['email'], data['phone']))
    conn.commit()
    contact_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': contact_id, 'name': data['name'], 'email': data['email'], 'phone': data['phone']}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)