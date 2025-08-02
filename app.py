from flask import Flask, request, render_template, redirect
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-5L4E2G3\\SQLEXPRESS;'
    'DATABASE=StudentDB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM Students")
    students = [dict(ID=row[0], Name=row[1], Email=row[2], Course=row[3]) for row in cursor.fetchall()]
    return render_template('form.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    cursor.execute("INSERT INTO Students (Name, Email, Course) VALUES (?, ?, ?)", (name, email, course))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    cursor.execute("DELETE FROM Students WHERE ID = ?", (student_id,))
    conn.commit()
    return redirect('/')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    cursor.execute("SELECT * FROM Students WHERE Name LIKE ?", ('%' + query + '%',))
    students = [dict(ID=row[0], Name=row[1], Email=row[2], Course=row[3]) for row in cursor.fetchall()]
    return render_template('form.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
