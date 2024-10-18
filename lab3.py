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