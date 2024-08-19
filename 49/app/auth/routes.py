from flask import render_template, redirect, url_for, request, flash, session
from app import mongo, bcrypt
from app.auth import auth
from bson.objectid import ObjectId

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = mongo.db.users.find_one({'username': username})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(password).decode('utf-8')
            mongo.db.users.insert_one({'username': username, 'password': hashpass})
            flash('You have successfully signed up!', 'success')
            return redirect(url_for('auth.login'))
        flash('Username already exists!', 'danger')

    return render_template('signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = mongo.db.users.find_one({'username': username})

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            flash('Login successful!', 'success')
            return redirect(url_for('auth.hello'))
        flash('Invalid username or password!', 'danger')

    return render_template('login.html')

@auth.route('/hello')
def hello():
    if 'user_id' in session:
        user_id = session['user_id']
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return render_template('hello.html', username=user['username'])
    return redirect(url_for('auth.login'))
