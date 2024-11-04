from flask import Flask, url_for, redirect, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5

import os

app=Flask(__name__) 

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

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
        </ol>
    </body>
    <footer>
        Бабий Арина Александровна, ФБИ-21, 3 Курс, 2024 год.
    </footer>
</html>
'''