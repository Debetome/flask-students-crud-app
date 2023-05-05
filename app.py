from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from random import choices
from random import randint
from string import ascii_letters
from string import digits

import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "".join(choices(ascii_letters + digits, k=randint(30, 40))) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

HOST = os.environ.get("HOST") if "HOST" in os.environ else "127.0.0.1"
PORT = int(os.environ.get("PORT")) if "PORT" in os.environ else 5000
PRODUCTION = bool(int(os.environ.get("PRODUCTION"))) if "PRODUCTION" in os.environ and os.environ.get("production") else False

class Student(db.Model):
    __tablename__ = "Students"
    id = db.Column("Id", db.Integer, primary_key=True, unique=True)
    name = db.Column("Name", db.String(30), unique=False)
    lastname = db.Column("Lastname", db.String(30), unique=False)
    dni = db.Column("DNI", db.Integer, unique=False)

@app.route("/", methods=["GET"])
@app.route("/students", methods=["GET"])
def students():
    students = list(Student.query.all())
    return render_template("students.html", students=students)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        dni = request.form["dni"]

        new_student = Student(
            name=name,
            lastname=lastname,
            dni=dni
        )

        if len(name) != 0 and len(lastname) != 0 and len(str(dni)) != 0:
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('students'))
        else:
            flash("There cannot be empty fields! ...")
            return redirect(url_for('create'))

    return render_template("create.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    student = Student.query.filter_by(id=id).first()
    if request.method == "POST":
        student.name = request.form["name"]
        student.lastname = request.form["lastname"]
        student.dni = request.form["dni"]

        if len(student.name) != 0 and len(student.lastname) != 0 and len(str(student.dni)) != 0:
            db.session.commit()
            return redirect(url_for('students'))
        else:
            flash("There cannot be empty fields! ...")
            return redirect(url_for('edit', id=id))

    return render_template("edit.html", student=student)

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id: int):
    Student.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('students'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=not PRODUCTION, port=PORT, host=HOST)