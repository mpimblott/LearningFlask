from flask import Flask, render_template, redirect, url_for, request # send_from_directory
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return redirect(url_for('login'))


@app.route('/hello')
def hello():
    return render_template('template.html', my_string="Go away!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/test')
def test():
    return render_template('test.html', my_string="Go away!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('hello'))
    return render_template('/login.html', error=error)


if __name__ == "__main__":
    app.run()

