from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from typing import Callable

app = Flask(__name__)


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Boolean: Callable


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = MySQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    is_complete = db.Column(db.Boolean)


db.create_all()


@app.get('/')
def home():
    todo_list = db.session.query(Todo).all()
    return render_template('base.html', todo_list=todo_list)


@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/update/<int:todo_id>')
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
