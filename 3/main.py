from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/<prof>')
@app.route('/training/<prof>')
def index(prof):
    if "инженер" == prof or "строитель" == prof:
        return render_template('prof.html', prof=prof.lower())
    else:
        return render_template('base.html', prof=prof.lower())

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')