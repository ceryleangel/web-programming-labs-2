from flask import Blueprint, redirect, render_template, request, make_response, redirect, session
lab4=Blueprint('lab4', __name__) 


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('/lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1') 
    x2 = request.form.get('x2') 
    
    if x1 == '' or x2 == '': 
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!') 
    if x2 == '0': 
        return render_template('lab4/div.html', error1='Делить на 0 нельзя!') 
    
    x1 = int(x1) 
    x2 = int(x2) 
    result = x1 / x2 
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('/lab4/sum-form.html')


@lab4.route('/lab4/sum', methods=['POST'])
def sum_function():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    # Преобразуем в 0, если поля пустые
    x1 = int(x1) if x1 else 0
    x2 = int(x2) if x2 else 0
    
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('/lab4/mul-form.html')


@lab4.route('/lab4/mul', methods=['POST'])
def mul_function():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    # Преобразуем в 1, если поля пустые
    x1 = int(x1) if x1 else 1
    x2 = int(x2) if x2 else 1

    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('/lab4/sub-form.html')


@lab4.route('/lab4/sub', methods=['POST'])
def sub_function():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('/lab4/pow-form.html')


@lab4.route('/lab4/pow', methods=['POST'])
def pow_function():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)

    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', error1='Невозможно возвести 0 в 0.')
    
    result = x1 ** x2
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)

tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET','POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut': 
        if tree_count > 0:  
            tree_count -= 1 
    elif operation == 'plant': 
        if tree_count < 12:  #
            tree_count += 1 
    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex John', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Kim', 'gender': 'male'},
    {'login': 'arina', 'password': '257', 'name': 'Arina Babii', 'gender': 'female'},
    {'login': 'robin', 'password': '000', 'name': 'Robert Smith', 'gender': 'male'},
]


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = next(user['name'] for user in users if user['login'] == login)
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')

    # Проверка на пустые поля
    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    # Поиск пользователя
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login  
            return redirect('/lab4/login') 

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')

    # Получаем температуру из формы
    temperature = request.form.get('temperature')

    if not temperature:
        error = 'Ошибка: не задана температура'
        return render_template('lab4/fridge.html', error=error)

    try:
        temp = float(temperature)
    except ValueError:
        error = 'Ошибка: температура должна быть числом'
        return render_template('lab4/fridge.html', error=error)

    snowflakes = None
    if temp < -12:
        message = 'Не удалось установить температуру — слишком низкое значение'
    elif temp > -1:
        message = 'Не удалось установить температуру — слишком высокое значение'
    elif -12 <= temp <= -9:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 3  # три снежинки
    elif -8 <= temp <= -5:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 2  # две снежинки
    elif -4 <= temp <= -1:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 1  # одна снежинка
    else:
        message = 'Неизвестная ошибка'

    return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)


corn = {
    'barley': {'name': 'ячмень', 'price': 12345},
    'oats': {'name': 'овёс', 'price': 8522},
    'wheat': {'name': 'пшеница', 'price': 8722},
    'rye': {'name': 'рожь', 'price': 14111}
}
@lab4.route('/lab4/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if not weight:
            message = "Ошибка: укажите вес заказа."
            return render_template('lab4/order.html', message=message)

        try:
            weight = float(weight)
        except ValueError:
            message = "Ошибка: вес должен быть числом."
            return render_template('lab4/order.html', message=message)

        if weight <= 0:
            message = "Ошибка: вес должен быть больше 0."
            return render_template('lab4/order.html', message=message)

        if weight > 500:
            message = "Ошибка: такого объёма сейчас нет в наличии."
            return render_template('lab4/order.html', message=message)


        grain_info = corn.get(grain)
        if not grain_info:
            message = "Ошибка: некорректный выбор зерна."
            return render_template('lab4/order.html', message=message)

        price_per_ton = grain_info['price']
        grain_name_ru = grain_info['name']
        total_price = weight * price_per_ton

        discount_message = None
        if weight > 50:
            discount = 0.1  # 10% скидка
            total_price *= (1 - discount)
            discount_message = "Применена скидка 10% за большой объём."

        message = f"Заказ успешно сформирован. Вы заказали {grain_name_ru}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб."

        return render_template('lab4/order.html', message=message, discount=discount_message)

    return render_template('lab4/order.html')