from flask import Flask, render_template, redirect, url_for, request, session  # abort # send_from_directory
from functools import wraps
import os
import accounts

app = Flask(__name__, static_url_path='/static')

user = accounts.create_account("Matthew", "password", True)

user_dictionary = {"Matthew": user}


# authenticate user username and password
def authenticate(login_username, login_password):
    account = user_dictionary.get(login_username)
    if account is None:
        return None
        print("invalid username")
    elif account.password == login_password:
        print("username: ", account.name)
        return account
    else:
        return None
        print("Invalid password")


# Decorator Function to check for login
def login_required(something):
    @wraps(something)
    def wrap(*args, **kwargs):
        if session.get('logged_in'):
            return something(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrap


# Decorator Function to check for login for admin
def admin_required(something):
    @wraps(something)
    def wrap(*args, **kwargs):
        username = session.get('username')
        account = user_dictionary.get(username)
        if session.get('logged_in') and account.is_admin:
            return something(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrap


# home page - redirects to login screen if not authenticated
@app.route('/')
@login_required
def home():
    return render_template('index.html', user=session['username'])


# logout - changes session value and redirects to login page
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


# login page - checks username and password against dictionary
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not session.get('logged_in'):
            account = authenticate(request.form['username'], request.form['password'])
            if account is None:
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                session['username'] = account.name
                return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))

    return render_template('/login.html', error=error)


@app.route('/admin')
@admin_required
def admin():
    return render_template('/admin.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()

