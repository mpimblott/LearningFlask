from flask import Flask, render_template, redirect, url_for, request, session, abort # send_from_directory
import os
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('test', my_string="Go away!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/boot')
def boot():
    return render_template('boot.html', my_string="Go away!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not session.get('logged_in'):
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
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

