from flask import Flask, render_template, redirect, url_for, request, session  # abort # send_from_directory
import os
import accounts

app = Flask(__name__, static_url_path='/static')

user = accounts.create_account("Matthew", "password", "1")

user_dictionary = {"Matthew": user}


# authenticate user username and password
def authenticate(login_username, login_password):
    account = user_dictionary.get(login_username)
    if account is None:
        return False
        print("invalid username")
    elif account.password == login_password:
        print("welcome back")
        session['username'] = login_username
        print("username: ", session['username'])
        return True
    else:
        return False
        print("Invalid password")


# home page - redirects to login screen if not authenticated
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
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
            if not authenticate(request.form['username'], request.form['password']):
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))

    return render_template('/login.html', error=error)


@app.route('/account')
def account():
    return render_template('/accountDashboard.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()

