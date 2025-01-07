import sqlite3

def create_connection():
	conn = sqlite3.connect('students.bd')
	return conn 

def create_table():
	conn = create_connection()	
	cursor = conn.cursor()
	cursor.execute("""
	CREATE TABLE IF NOT EXISTS students (
		id INTEGER PRIMARY KEY AUTOINCREMENT, 
		name TEXT,
		age INTEGER,
		gender TEXT,
		course TEXT
	)
	""")
	conn.commit()
	conn.close()


def add_student(name, age, gender, course):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute(''' INSERT INTO students (name, age, gender, course) VALUES (?, ?, ?, ?)
	''', (name, age, gender, course))
	conn.commit()
	conn.close()

def get_all_students():
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM students')
	students = cursor.fetchall()
	conn.close()
	return students


def update_student(student_id, name, age, gender, course):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute('''
	UPDATE students
	SET name = ?, age = ?, gender = ?, course = ?
	WHERE id = ?
	''', (name, age, gender, course, student_id))
	conn.commit()
	conn.close()


def delete_student(student_id):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute('DELETE FROM students WHERE id = ?',(student_id,))
	conn.commit()
	conn.close()


def select_student(studen_id):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM students WHERE id LIKE > %0")
	students = cursor.fetchone()
	return students