from flask import Flask, url_for, redirect, render_template
from lab1 import lab1
from lab2 import lab2
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from rgz import rgz

import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users, articles
from flask_login import LoginManager

app=Flask(__name__) 

login_manager=LoginManager()
login_manager.login_view='lab8.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'sicret123')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')


if app.config['DB_TYPE'] == 'postgres':
    db_user = 'arina_babii_orm'
    db_password = '987'
    db_name = 'arina_babii_orm'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "arina_babii_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)
    
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(rgz)

@app.errorhandler(404)
def not_found(err):
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <tytle>Ошибка 404</tytle>
    </head>
    <body>
        <h1>Упс… Кажется такой страницы не существует</h1>
        <p>Сервер не может найти запрошенный ресурс. В браузере это означает,
        что URL-адрес не распознан. В API это также может означать,
        что адрес правильный, но ресурс не существует.</p>

        <img src="''' + url_for('static', filename='lab1/eror404.webp') + '''" style="width: 300px;
        position: absolute; top: 60%; right: 50px; transform: translateY(-50%);"></br>

        <a href="/">Вернуться на главную</a>
    </body>
''', 404

@app.errorhandler(500)
def internal_server_error(err):
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <tytle>Ошибка 500</tytle>
    </head>
    <body>
        <h1>Внутренняя ошибка сервера</h1>
        <p>На сервере произошла ошибка, в результате которой он не может успешно обработать запрос.
        Пожалуйста, попробуйте позже.</p>

        <a href="/">Вернуться на главную</a>
    </body>
</html>
''', 500

@app.route('/')
@app.route('/index')
def index():
    return '''
<!doctype html>
<html>
    <head>
        <tytle>НГТУ, ФБ, Лабораторные работы</tytle>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='main.css') + '''">
    </head>
    <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
        <ol>
            <li><a href="/lab1">Первая Лабораторная</a></li>
            <li><a href="/lab2">Вторая Лабораторная</a></li>
            <li><a href="/lab3">Третья Лабораторная</a></li>
            <li><a href="/lab4">Четвертая Лабораторная</a></li>
            <li><a href="/lab5">Пятая Лабораторная</a></li>
            <li><a href="/lab6">Шестая Лабораторная</a></li>
            <li><a href="/lab7">Седьмая Лабораторная</a></li>
            <li><a href="/lab8">Восьмая Лабораторная</a></li>
            <li><a href="/lab9">Девятая Лабораторная</a></li>
            <li><a href="/rgz">РГЗ</a></li>
        </ol>
    </body>
    <footer>
        Бабий Арина Александровна, ФБИ-21, 3 Курс, 2024 год.
    </footer>
</html>
'''