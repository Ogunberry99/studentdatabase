import streamlit as st
from db import create_table, add_student, get_all_students, update_student, delete_student, create_connection
create_table()

st.title("Student Management System")

menu = ["Add Student", "View Students", "Edit Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

def search_students(query):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM students WHERE name LIKE ? OR course LIKE ?", ('%'+query+'%', '%'+query+'%'))
	students = cursor.fetchall()
	return students

def select_student(student_id):
	conn = create_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM students WHERE id LIKE > %0")
	students = cursor.fetchone()
	return students

if choice == "Add Student":
	st.subheader("Add New Student")
	name = st.text_input("Name")
	age = st.number_input("Age", min_value=1, max_value=100, step=1)
	gender = st.selectbox("Gender", ["Male", "Female", "Other"])
	course = st.text_input("Course")

	if st.button("Add Student"):
		if not name or not course:
			st.error("Please fill all the fields.")
		else:
			add_student(name, age, gender, course)
			st.success(f"Added {name} to the student database.")

elif choice == "View Students":
	st.subheader("View All Students")

	search_query = st.text_input("Search by Name or Course")
	if st.button("Search"):
		students = search_students(search_query)
		if students:
			for student in students:
				st.text(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Gender: {student[3]} | Course: {student[4]}")
		else:
			st.error("No students found.")

	else:
		students = get_all_students()
		for student in students:
			st.text(f"ID: {student[0]} | Name {student[1]} | Age: {student[2]} | Gender: {student[3]} | Course: {student[4]}")

elif choice == "Edit Student":
	st.subheader("Edit Student Details")
	student_id = st.number_input("Enter Student ID", min_value=1)
	name = st.text_input("Enter Name")
	age = st.number_input("Enter Age")
	gender = st.selectbox("Gender", ["Male", "Female", "Other"])
	course = st.text_input("Enter Course")
	if st.button("Update Info"):
		update_student(student_id, name, age, gender, course)
		st.success("Update Successful")
	else:
		st.error("Student not found.")

elif choice == "Delete Student":
	st.subheader("Delete Student")
	student_id = st.number_input("Enter Student ID", min_value=1)

	if st.button("Delete"):
		delete_student(student_id)
		st.success(f"Deleted student with ID {student_id}.")





