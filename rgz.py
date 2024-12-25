from flask import Blueprint, redirect, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, recipes
from flask_login import login_user, login_required, current_user, logout_user
import re

rgz = Blueprint('rgz', __name__)


@rgz.route('/rgz/')
def lab():
    if current_user.is_authenticated:
        return render_template('rgz/rgz.html', login=current_user.login)
    return render_template('rgz/rgz.html')


@rgz.route('/rgz/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template('rgz/register.html', message='Вы не можете зарегистрироваться, находясь в аккаунте. Хотите выйти?', login=current_user.login)
    
    if request.method == 'POST':
        login_form = request.form['login']
        password_form = request.form['password']

        if login_form == '':
            return render_template('rgz/register.html', error='Заполните имя пользователя')

        if password_form == '':
            return render_template('rgz/register.html', error='Заполните пароль')
        
        valid_pattern = re.compile(r'^[a-zA-Z0-9!\"#$%&\'()*+,-./:;<=>?@[\\$$^_`{|}~]+$')

        # Проверка на валидность логина
        if not valid_pattern.match(login_form):
            return render_template('rgz/register.html', error='Имя пользователя может содержать только латинские буквы, цифры и знаки препинания.')

        # Проверка на валидность пароля
        if not valid_pattern.match(password_form):
            return render_template('rgz/register.html', error='Пароль может содержать только латинские буквы, цифры и знаки препинания.')

        login_exists = users.query.filter_by(login=login_form).first()
        if login_exists:
            return render_template('rgz/register.html', error='Такой пользователь уже существует')

        password_hash = generate_password_hash(password_form)
        new_user = users(login=login_form, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember=False)
        return redirect('/rgz/login')

    return render_template('rgz/register.html')


@rgz.route('/rgz/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('rgz/success_login.html', login=current_user.login)
    
    if request.method == 'POST':
        login_form = request.form['login']
        password_form = request.form['password']

        if login_form == '':
            return render_template('rgz/login.html', error='Заполните имя пользователя')

        if password_form == '':
            return render_template('rgz/login.html', error='Заполните пароль')

        user = users.query.filter_by(login=login_form).first()
        if user and check_password_hash(user.password, password_form):
            login_user(user)
            return redirect('/rgz/login')

        return render_template('rgz/login.html', error='Неверный логин или пароль')

    return render_template('rgz/login.html')


@rgz.route('/rgz/logout')
@login_required
def logout():
    logout_user()
    return redirect('/rgz/')


@rgz.route('/rgz/recipes', methods=['GET'])
def recipe():
    page = request.args.get('page', 1, type=int)
    title_filter = request.args.get('title')
    ingredients_filter = request.args.get('ingredients')
    mode = request.args.get('mode', 'any')

    query = recipes.query

    
    # Проверка фильтра по ингредиентам
    if ingredients_filter:
        ingredients = ingredients_filter.split(',') 
        if mode == 'all':
            for ingredient in ingredients:
                query = query.filter(recipes.ingredients.ilike(f"%{ingredient.strip()}%"))
        elif mode == 'any':
            # Создаем фильтр для любого из ингредиентов
            # Используем reduce для создания составного OR условия
            from sqlalchemy import or_

            or_conditions = [recipes.ingredients.ilike(f"%{ingredient.strip()}%") for ingredient in ingredients]
            query = query.filter(or_(*or_conditions))

    if title_filter:
        query = query.filter(recipes.title.ilike(f'%{title_filter}%'))

    paginated_recipes = query.paginate(page=page, per_page=20, error_out=False)

    if current_user.is_authenticated:
        return render_template('rgz/recipe.html', recipes=paginated_recipes, login=current_user.login)
    return render_template('rgz/recipe.html', recipes=paginated_recipes)


@rgz.route('/rgz/create_recipe', methods=['GET', 'POST'])
@login_required
def create_recipe():
    if current_user.login != 'Admin':
        return redirect('/rgz/recipes')

    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        photo_url = request.form['photo_url']

        new_recipe = recipes(title=title, ingredients=ingredients, steps=steps, photo_url=photo_url)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect('/rgz/recipes')

    return render_template('rgz/create_recipe.html', login=current_user.login)


@rgz.route('/rgz/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    if current_user.login != 'Admin':
        return redirect('/rgz/recipes')

    recipe = recipes.query.get(recipe_id)

    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.ingredients = request.form['ingredients']
        recipe.steps = request.form['steps']
        recipe.photo_url = request.form['photo_url']

        db.session.commit()
        return redirect('/rgz/recipes')

    return render_template('rgz/edit_recipe.html', recipe=recipe, login=current_user.login)


@rgz.route('/rgz/delete_recipe/<int:recipe_id>', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    if current_user.login != 'Admin':
        return redirect('/rgz/recipes')

    recip = recipes.query.get(recipe_id)
    db.session.delete(recip)
    db.session.commit()
    return redirect('/rgz/recipes')


@rgz.route('/rgz/delete_account', methods=['POST'])
@login_required
def delete_account():
    # Получаем текущего пользователя
    user = current_user
    # Удаляем пользователя из базы данных
    db.session.delete(user)  # Удаляем пользователя из сессии
    db.session.commit()  # Сохраняем изменения

    logout_user()  # Выход из текущего аккаунта
    return redirect('/rgz/') 