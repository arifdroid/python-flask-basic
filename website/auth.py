from crypt import methods
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form

    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully', category='success')
                return redirect(url_for('views.home'))

            else:
                flash('Incorrect password', category='error')

        else:
            flash('Email does not exist', category='error')

    return render_template('login.html', text="Testing")


@auth.route('/logout')
def logout():
    return render_template('login.html')


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist', category="error")
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category="error")
        elif len(firstname) < 2:
            flash('First name must be greater than 2 characters', category="error")
        elif len(password) < 5:
            flash('Passwod must be greater than 5 characters', category="error")
        else:
            new_user = User(email=email, first_name=firstname,
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category="success")
            return redirect(url_for('views.home'))
        # add user to database

    return render_template('sign_up.html')
