from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/hello/')
def hello():
    return render_template('template.html', my_string="Go away!", my_list=[0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    # app.debug = True
    app.run()
    # app.run(debug=True)
