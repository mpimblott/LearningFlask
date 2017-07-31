from flask import Flask, render_template, redirect, url_for, request, session  # abort # send_from_directory
import os
app = Flask(__name__, static_url_path='/static')

user_dictionary = {"Matthew": "password"}


def authenticate(login_username, login_password):
    if user_dictionary.get(login_username) is None:
        return False
        print("invalid username")
    elif user_dictionary.get(login_username) == login_password:
        print("welcome back")
        session['username'] = login_username
        print("username: ", session['username'])
        return True
    else:
        return False
        print("Invalid password")


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('index.html', user=session['username'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not session.get('logged_in'):
            if not authenticate(request.form['username'], request.form['password']):
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                return redirect(url_for('home'))
        else:
            error = 'already logged in'

    return render_template('/login.html', error=error)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()

