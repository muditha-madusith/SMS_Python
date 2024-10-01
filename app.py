from flask import Flask, request, render_template, jsonify
import pymysql
from config import MYSQL

app = Flask(__name__)

# MySQL connection
def get_db_connection():
    conn = pymysql.connect(
        host=MYSQL['host'],
        user=MYSQL['user'],
        password=MYSQL['password'],
        database=MYSQL['database'],
        cursorclass=pymysql.cursors.DictCursor  # Use DictCursor for dictionary output
    )
    return conn

# Routes for students management
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students)

@app.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = %s', (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    name = new_student['name']
    age = new_student['age']
    grade = new_student['grade']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)',
                   (name, age, grade))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    student_data = request.get_json()
    name = student_data['name']
    age = student_data['age']
    grade = student_data['grade']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s',
                   (name, age, grade, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Student updated successfully'})

@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Student deleted successfully'})


# UI route
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
