# 🎓 Student Registration System (Flask + SQL Server)

A clean and functional full-stack web application that allows users to register, search, and delete student records. The app is built with **Flask (Python)** on the backend, **HTML/CSS + Bootstrap** for the frontend, and **SQL Server** for persistent data storage.

---

## 📌 Features

- 📝 Register new students (Name, Email, Course)
- 🔍 Search students by name (partial matches supported)
- 🗑️ Delete students from the database
- 📋 View all registered students in a formatted table
- 💡 Responsive and modern UI with Bootstrap
- 🔐 Secure, parameterized SQL queries (protection from SQL injection)

---

## 🛠️ Tech Stack

| Layer       | Technology             |
|-------------|------------------------|
| Frontend    | HTML, CSS, Bootstrap   |
| Backend     | Flask (Python)         |
| Database    | Microsoft SQL Server   |
| Connector   | `pyodbc`               |
| Server Type | Localhost (Development Server) |

---


---

## 🚀 How to Run Locally

### ✅ Prerequisites

- Python 3.x installed
- SQL Server (local or remote instance)
- Python packages: Flask and pyodbc

Install packages:
```bash
pip install flask pyodbc

----------------------------
 Database Setup
Open SQL Server Management Studio.

Create a database:
sql

CREATE DATABASE StudentDB;
GO
USE StudentDB;

CREATE TABLE Students (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100),
    Email VARCHAR(100),
    Course VARCHAR(100)
);

Running the App
Make sure your connection string in app.py matches your system:

python
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-5L4E2G3\\SQLEXPRESS;'
    'DATABASE=StudentDB;'
    'Trusted_Connection=yes;'
)

Then, start the app:

bash
python app.py

 Author
Veesha Fatima
Passionate about Python, Web Development, and building smart systems.
## 📂 Project Structure

