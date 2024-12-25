from flask import Blueprint, render_template,redirect, request
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

lab8=Blueprint('lab8',__name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('lab8/register.html')
    
    login_form=request.form.get('login')
    password_form=request.form.get('password')

    if not login_form or not password_form:
        return render_template('lab8/register.html', error='Логин и пароль не могут быть пустыми')
    
    login_exists=users.query.filter_by(login=login_form).first()
    
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')

    password_hash=generate_password_hash(password_form)
    new_user=users(login=login_form,password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=False)
    return redirect ('/lab8/')    


@lab8.route('/lab8/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('lab8/login.html')
    
    login_form=request.form.get('login')
    password_form=request.form.get('password')

    remember = request.form.get('remember')

    if not login_form or not password_form:
        return render_template('lab8/login.html', error='Логин и пароль не могут быть пустыми', login=login_form)
    
    user=users.query.filter_by(login=login_form).first()

    if user:
        if check_password_hash(user.password, password_form):
            login_user(user,remember=remember)
            return redirect('/lab8/')

    return render_template('lab8/login.html',error='Ошибка входа: логин и/или пароль неверны', login=login_form)    

@lab8.route('/lab8/articles')
@login_required
def article_list():
    article_list = articles.query.all() 
    return render_template('lab8/articles.html',articles=article_list)

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/create',methods=['GET','POST'])
@login_required
def create():
    if request.method=='GET':
        return render_template('lab8/create_articles.html')
    
    title=request.form.get('title')
    article_text=request.form.get('article_text')

    if not title or not article_text:
        return render_template('lab8/create_articles.html', error='Заполните все поля')

    article=articles(title=title,article_text=article_text,login_id=current_user.id)
    db.session.add(article)
    db.session.commit()

    return redirect('/lab8/')

@lab8.route('/lab8/redact/<int:id>',methods=['GET', 'POST'])
@login_required
def redact(id):

    article = articles.query.get(id)
    
    if request.method == 'POST':
        title = request.form.get('title')
        article_text = request.form.get('article_text')

        if not title or not article_text:
            return render_template('lab8/redact.html', error='Заголовок и текст статьи обязательны!')

        # Обновляем статью
        article.title = title
        article.article_text = article_text
        db.session.commit()
        return redirect('/lab8/articles')
    
    return render_template('lab8/redact.html', articles=article)


@lab8.route('/lab8/delete', methods=['POST'])
@login_required
def delete_article():
    id = request.form.get('id')
    article = articles.query.get(id) 
    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/articles')