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

        <img src="''' + url_for('static', filename='eror404.webp') + '''" style="width: 300px;
        position: absolute; top: 60%; right: 50px; transform: translateY(-50%);"></br>

        <a href="/">Вернуться на главную</a>
    </body>
''', 404

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

@app.errorhandler(500)
def internal_server_error(err):
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
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

@app.route('/lab1/trigger_500')
def trigger_500():
    abort(500)

@app.route('/lab1/an_error')
def make_an_error():
    return 1 / 0

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
    <div class="container" style='display: flex; justify-content: space-between;'>
            <div class="rout_list" style='width: 30%; margin-left: 5px'>
                <h2>Список rout'ов:</h2>
                <ol>
                    <li><a href="/index">/index</a></li>
                    <li><a href="/lab1/web">/lab1/web</a></li>
                    <li><a href="/lab1/info">/lab1/info</a></li>
                    <li><a href="/lab1/oak">/lab1/oak</a></li>
                    <li><a href="/lab1/counter">/lab1/counter</a></li>
                    <li><a href="/lab1/new_route">/lab1/new_route</a></li>
                    <li><a href="/lab1/resource">/lab1/resource (дополнительное задание)</a></li>
                </ol>
            </div>

            <div class="error_list" style='width: 68%;'>
                <h2>Список ошибок:</h2>
                <ol>
                    <li><a href="/lab1/trigger_400">400</a></li>
                    <li><a href="/lab1/trigger_401">401</a></li>
                    <li><a href="/lab1/trigger_403">403</a></li>
                    <li><a href="/lab1/trigger_404">404</a></li>
                    <li><a href="/lab1/trigger_405">405</a></li>
                    <li><a href="/lab1/trigger_418">418</a></li>
                    <li><a href="/lab1/trigger_500">500</a></li>
                </ol>
            </div>
        </div>
    </body>
    <footer>
        Бабий Арина Александровна, ФБИ-21, 3 Курс, 2024 год.
    </footer>
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
    return redirect("/lab1/author")

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

@app.route('/lab1/new_route')
def new_route():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <tytle>The three little pigs</tytle>
    </head>
    <body>
        <p>Sergey Mihalcov</p>
        <div class="text_container" style='width: 50%'>
            <p style='margin-top: 10px'> The three little pigs are brothers. They are going into the forest. They want to build three houses. 
            "Let’s build our houses here," says the first little pig, Percy. "Yes," says the second little pig, Peter. 
            "That’s a good idea," says the third little pig, Patrick. The first little pig, Percy, gets some straw and he starts to build a house of straw. 
            He sings, "Hum de hum, dum de dum, hee de dum, dee de hum," when he works.</p>

            <p>The second little pig, Peter, gets some wood and he starts to build a house of wood. He sings, 
            "Hum de hum, dum de dum, hee de dum, dee de hum," when he works. The third pig, Patrick, is very clever. 
            He gets some bricks and he starts to build a house of bricks. He sings, "Hum de hum, dum de dum, hee de dum, dee de hum," 
            when he works. Now all the houses are ready. The three little pigs make a fence and they paint it red.</p>

            <p> But a big bad wolf lives in the forest. Every day the wolf watches the pigs. He is hungry and he wants to eat them. 
            He looks at the house of straw and he says, "I can smell a little pig. I want to eat him for my dinner,". The big bad wolf 
            jumps over the red fence. He goes to the house of straw and he knocks on the door. "Can I come in, little pig? I’m not very big!" 
            he says. But Percy sees it is a big bad wolf. He says, "Go away! You can’t come in. You’re a big bad wolf, you horrible thing."</p>

        </div>

        <div class="image_container" style='position: absolute; right: 50px; top: 10%'>
            <img src="''' + url_for('static', filename='nif.jpg') + '''" style='margin-top: 10px'>
        </div>

        <div>
        <a href="/lab1">Назад на страницу лабораторной</a>
        </div>
    </body>
    <footer>Бабий Арина Александровна, ФБИ-21, 3 Курс, 2024 год.</footer>
</html>
''', 200, {
    'Content-Language': 'en',
    'X-Nerd': '42',
    'X-Student': 'Babii Arina'
}