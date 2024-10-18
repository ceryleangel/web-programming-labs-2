from flask import Blueprint, url_for, redirect, render_template, request
lab2=Blueprint('lab2', __name__) 


@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list =  [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 80},
    {'name': 'Незабудка', 'price': 50},
    {'name': 'Ромашка', 'price': 30}
]

#Меню всех цветов
@lab2.route('/lab2/all_flowers/')
def all_flowers():
    flowers = flower_list
    flowers_num = len(flower_list)
    return render_template('flowers.html', flower_list=flowers, flowers_num=flowers_num)
  
@lab2.route('/lab2/add_flower/')
def add_flowers():
    name = request.args.get('name')
    price = request.args.get('price')
    style = url_for("static", filename="main.css")
    if name and price:
        flower_list.lab2end({'name': name, 'price': int(price)})
        flower_id = len(flower_list) - 1
        return render_template('add_flower.html', flower_id=flower_id, name=name, price=price)
    else:    
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Поле не заполнено!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 400

#Цветок по ID
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    style = url_for("static", filename="main.css")
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Такого цветка нет!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 404
    else:
        flower = flower_list[flower_id]
    return render_template('flower_id.html', flower=flower, flower_id=flower_id)


#Не задан ID цветка
@lab2.route('/lab2/flowers/')
def err_flowers():
    style = url_for("static", filename="main.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Вы не задали ID цветка!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 400
    
#Очистить весь список цветов
@lab2.route('/lab2/delete_flowers/')
def delete_flowers():
    flower_list.clear()  
    return redirect('/lab2/all_flowers/')

#Удалить цветок по ID
@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    style = url_for("static", filename="main.css")
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Цветов больше нет!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 404
    else:
        del flower_list[flower_id]
        return redirect('/lab2/all_flowers/')


@lab2.route('/lab2/exemple')
def example():
    number = '2'
    kurs = '3'
    name ='Арина Бабий'
    num_gr='21'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'апельсины', 'price': 120},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 300},
        {'name': 'бананы', 'price': 150},
        ]
    return render_template('exemple.html', name=name, number=number, kurs=kurs, num_gr=num_gr, fruits=fruits)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = 'О <b> сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html', phrase=phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    num_a = a
    num_b = b
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Деление на ноль"
    power = a ** b
    return render_template('calc.html', a=num_a, b=num_b, addition=addition, subtraction=subtraction,
                           multiplication=multiplication, division=division, power=power)


@lab2.route('/lab2/calc/')
def red_calc():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def redi_calc(a):
    return redirect(f'/lab2/calc/{a}/1')

books = [
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Роман", "pages": 382},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 680},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 384},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 528},
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Aнтиутопия", "pages": 320},
    {"author": "Марк Твен", "title": "Приключения Тома Сойера", "genre": "Повесть", "pages": 336},
    {"author": "Дж. Д. Сэлинджер", "title": "Над пропастью во ржи", "genre": "Роман", "pages": 224},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
    {"author": "Иван Тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 416},
    {"author": "Михаил Хазин", "title": "Лестница в небо", "genre": "Научно-популярный", "pages": 624}
]

@lab2.route('/lab2/books/')
def book():
    return render_template('book.html', books=books)

dogs = [
    {
        "name": "Собака-наблюдака",
        "description": "Отличительная особенность собаки-наблюдаки — ее глаза. Они всегда смотрят на вас и видят все.",
        "image": "dog1.jpg"
    },
    {
        "name": "Собака-после-работы-уставака",
        "description": "Главная особенность Собаки-после-работы-уставаки — постоянный сон. Примечание: купите беруши, она так же громко храпит",
        "image": "dog2.jpg" 
    },
    {
        "name": "Собака-во-все-дырки-залезака",
        "description": "Собака-во-все-дырки-залезака - способна залезть куда угодно, чтобы выполнить функцию Собаки-после-работы-уставаки",
        "image": "dog6.jpg"
    },
    {
        "name": "Собака-обижака",
        "description": "Собака-обижака - обижается на вас до тех пор, пока вы не начнете есть. Потом обида пропадает. На время пока у вас есть еда.",
        "image": "dog4.jpg"
    },
    {
        "name": "Собака-бесяку-поймака",
        "description": "Собака-бесяку-поймака - летает как ракета. Залижит досмерти",
        "image": "dog5.jpg"
    }
]

@lab2.route('/lab2/dogs/')
def dog():
    return render_template('dogs.html', dogs=dogs)

