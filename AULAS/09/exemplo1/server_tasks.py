from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicializar banco de dados
def init_db():
    conn = sqlite3.connect('AULAS/09/exemplo1/tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, completed BOOLEAN)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('AULAS/09/exemplo1/tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = [{'id': row[0], 'task': row[1], 'completed': bool(row[2])} for row in cursor.fetchall()]
    conn.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = sqlite3.connect('AULAS/09/exemplo1/tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (data['task'], False))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': task_id, 'task': data['task'], 'completed': False}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('AULAS/09/exemplo1/tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tarefa removida'})

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    conn = sqlite3.connect('AULAS/09/exemplo1/tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (True, task_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tarefa concluída'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)