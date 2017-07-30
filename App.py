from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def main():
    return 'Hello World'

if __name__ == '__main__':
    # app.debug = True
    app.run()
    # app.run(debug=True)
