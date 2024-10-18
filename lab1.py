from flask import Blueprint, Flask, url_for, redirect, render_template
lab1=Blueprint('lab1', __name__) 


@lab1.route('/lab1/error/400')
def error_400():
    return '''
<!doctype html>
<html>
    <head>
        <title>Код 400</title>
    </head>
    <body>
        <h1>400 Bad Request</h1>
        <p>Сервер не может или не будет обрабатывать запрос из-за очевидной ошибки клиента.</p>
    </body>
</html>
''', 400


@lab1.route('/lab1/error/401')
def error_401():
    return '''
<!doctype html>
<html>
    <head>
        <title>Код 401</title>
    </head>
    <body>
        <h1>401 Unauthorized</h1>
        <p>Запрос не был применен, так как отсутствуют действительные учетные данные для целевого ресурса.</p>
    </body>
</html>
''', 401


@lab1.route('/lab1/error/402')
def error_402():
    return '''
<!doctype html>
<html>
    <head>
        <title>Код 402</title>
    </head>
    <body>
        <h1>402 Payment Required</h1>
        <p>Этот код зарезервирован для будущего использования.</p>
    </body>
</html>
''', 402


@lab1.route('/lab1/error/403')
def error_403():
    return '''
<!doctype html>
<html>
    <head>
        <title>Код 403</title>
    </head>
    <body>
        <h1>403 Forbidden</h1>
        <p>У клиента нет прав доступа к содержимому, поэтому сервер отказывается дать надлежащий ответ.</p>
    </body>
</html>
''', 403


@lab1.route('/lab1/error/405')
def error_405():
    return '''
<!doctype html>
<html>
    <head>
        <title>Код 405</title>
    </head>
    <body>
        <h1>405 Method Not Allowed</h1>
        <p>Метод, указанный в запросе, не разрешен для указанного ресурса.</p>
    </body>
</html>
''', 405


@lab1.route('/lab1/error/418')
def error_418():
    return '''
<!doctype html>
<html>
    <head>
        <title>Код 418</title>
    </head>
    <body>
        <h1>418 I'm a teapot</h1>
        <p>Сервер отказывается варить кофе, потому что является чайником.</p>
    </body>
</html>
''', 418


@lab1.route('/lab1/trigger_500')
def trigger_500():
    abort(500)


@lab1.route('/lab1/an_error')
def make_an_error():
    return 1 / 0


@lab1.route('/lab1')
def lab():
    return'''
<!doctype html>
<html>
    <head>
        <tytle>Лабораторная 1</tytle>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
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
                    <li><a href="/lab1/error/400">400</a></li>
                    <li><a href="/lab1/error/401">401</a></li>
                    <li><a href="/lab1/error/402">402</a></li>
                    <li><a href="/lab1/error/403">403</a></li>
                    <li><a href="/lab1/error/404">404</a></li>
                    <li><a href="/lab1/error/405">405</a></li>
                    <li><a href="/lab1/error/418">418</a></li>
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
 

@lab1.route("/lab1/web") 
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


@lab1.route("/lab1/author")
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


@lab1.route('/lab1/oak')
def oak():
    path = url_for("static", filename="lab1/oak.jpg")
    style = url_for('static', filename='lab1/lab1.css')
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


@lab1.route('/lab1/counter')
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


@lab1.route('/lab1/counter_cleaner')
def counter_cleaner():
    global count
    count = 0
    return redirect('/lab1/counter')


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
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


@lab1.route('/lab1/new_route')
def new_route():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
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
            <img src="''' + url_for('static', filename='lab1/nif.jpg') + '''" style='margin-top: 10px'>
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