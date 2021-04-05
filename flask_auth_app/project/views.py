from flask import Flask, request, render_template, redirect, app
from flask_login import (
    login_required, current_user,
    login_user, UserModel, logout_user)


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')

    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email=email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/index')

    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        if UserModel.query.filter_by(email=email):
            return ('Email already Present')

        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
