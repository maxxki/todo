from flask import Flask, request, jsonify
import mysql

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ToDoAppDB"
)
cursor = db.cursor()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (data['title'], data['description']))
    db.commit()
    return jsonify({"message": "Task added"}), 201

if __name__ == '__main__':
    app.run(debug=True)
