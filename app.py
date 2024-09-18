from flask import Flask, url_for, redirect
app=Flask(__name__) 

@app.errorhandler(400)
def bad_request(err):
    return '''Ошибка 400.
    Неверный запрос. Сервер не может обработать запрос из-за чего-то,
    что воспринимается как ошибка клиента (например, неправильный синтаксис, формат
    или маршрутизация запроса).''', 400

@app.route('/lab1/trigger_400')
def trigger_400():
    abort(400)

@app.errorhandler(401)
def unauthorized(err):
    return '''Ошибка 401. Для доступа к ресурсу требуется аутентификация.
    Клиент должен передать заголовок Authorization в запросе.''', 401

@app.route('/lab1/trigger_401')
def trigger_401():
    abort(401)

class PaymentRequired(HTTPException):
    code = 402
    description = 'Payment Required'

@app.errorhandler(PaymentRequired)
def payment_required(err):
    return '''Ошибка 402. Зарезервировано для будущего использования.
    Используется для целей тестирования оплаты.''', 402

@app.route('/lab1/trigger_402')
def trigger_402():
    abort(402)

@app.errorhandler(403)
def forbidden(err):
    return '''Ошибка 403. Клиент не имеет прав доступа к содержимому,
    поэтому сервер отказывает в выполнении запроса.''', 403

@app.route('/lab1/trigger_403')
def trigger_403():
    abort(403)

@app.errorhandler(404)
def not_found(err):
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <tytle>Ошибка 404</tytle>
    </head>
    <body>
        <h1>Упс… Кажется такой страницы не существует</h1>
        <p>Сервер не может найти запрошенный ресурс. В браузере это означает,
        что URL-адрес не распознан. В API это также может означать,
        что адрес правильный, но ресурс не существует.</p>

        <img src="''' + url_for('static', filename='Error_404_img.png') + '''" style="width: 300px;
        position: absolute; top: 60%; right: 50px; transform: translateY(-50%);"></br>

        <a href="/">Вернуться на главную</a>
    </body>
''', 404

@app.route('/lab1/trigger_404')
def trigger_404():
    abort(404)

@app.errorhandler(405)
def method_not_allowed(err):
    return '''Ошибка 405. Метод, указанный в запросе (например, POST, PUT, DELETE) не применим к ресурсу,
    и сервер не поддерживает его.''', 405

@app.route('/lab1/trigger_405')
def trigger_405():
    abort(405)

@app.errorhandler(418)
def i_am_a_teapot(err):
    return '''Ошибка 418. Я… я – чайник? ''', 418

@app.route('/lab1/trigger_418')
def trigger_418():
    abort(418)

@app.route('/')
@app.route('/index')
def index():
    return '''
<!doctype html>
<html>
    <head>
        <tytle>НГТУ, ФБ, Лабораторные работы</tytle>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
        <ol>
            <li><a href="/lab1">Первая Лабораторная</a></li>
        </ol>
    </body>
    <footer>
        Бабий Арина Александровна, ФБИ-21, 3 Курс, 2024 год.
    </footer>
</html>
'''

@app.route('/lab1')
def lab1():
    return'''
<!doctype html>
<html>
    <head>
        <tytle>Лабораторная 1</tytle>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Flask</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python,
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится
        к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений,
        сознательно предоставляющих лишь самые базовые возможности.</p>

        <a href="/">Назад на главную</a></li>
    </body>
</html>
'''
 
@app.route("/lab1/web") 
def web(): 
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
               <a href="/author">author</a>
           </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Бабий Арина Александровна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    style = url_for('static', filename='lab1.css')
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''
count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count +=1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
    </body>
</html>
'''

@app.route('/lab1/counter_cleaner')
def counter_cleaner():
    global count
    count = 0
    return redirect('/lab1/counter')

@app.route("/lab1/info")
def info():
    return redirect("/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </div>
</html>    
''', 201