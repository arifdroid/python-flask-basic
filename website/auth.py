from crypt import methods
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
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

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category="erorr")
        elif len(firstname) < 2:
            flash('First name must be greater than 2 characters', category="erorr")
        elif len(password) < 5:
            flash('Passwod must be greater than 5 characters', category="erorr")
        else:
            flash('Account Created', category="success")
        # add user to database

    return render_template('sign_up.html')
