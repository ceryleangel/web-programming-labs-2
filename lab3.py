from flask import Blueprint, Flask, url_for, redirect, request, render_template, make_response
lab3=Blueprint('lab3', __name__) 

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')
    return render_template('lab3/lab3.html', name=name, name_color = name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Arina', max_age=5)
    resp.set_cookie('age', '20', max_age=5)
    resp.set_cookie('name_color', 'magenta', max_age=5)
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user = user, age=age, sex=sex, errors = errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    #Добавка молока удорожает напиток на 30 рублей, а сахара - на 10.
    if request.args.get('milk') == 'on':
        price += 30 
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')  
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    backgroundcolor = request.args.get('background-color')
    fontsize = request.args.get('fontsize')
    fontweight = request.args.get('fontweight')

    resp = make_response(redirect('/lab3/settings'))

    if color:
        resp.set_cookie('color', color)
    
    if backgroundcolor:
        resp.set_cookie('background-color', backgroundcolor)
    
    if fontsize:
        resp.set_cookie('fontsize', fontsize)

    if fontweight:
        resp.set_cookie('fontweight', fontweight)

    if not (color or backgroundcolor or fontsize or fontweight):
        color = request.cookies.get('color')
        backgroundcolor = request.cookies.get('background-color')
        fontsize = request.cookies.get('fontsize')
        fontweight = request.cookies.get('fontweight')
        resp = make_response(render_template('lab3/settings.html', color=color, backgroundcolor=backgroundcolor, fontsize=fontsize, fontweight=fontweight))
    return resp


