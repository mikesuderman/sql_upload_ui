from flask import Flask, render_template, request, url_for, flash, redirect
from data import NewRow

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your secret key'

# my_cols = 'date','cost','type','amount','unit','comment'

types = [
    'toronto_hydro',
    'enbridge'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        date = request.form['date']
        cost = request.form['cost']
        t = request.form['type']
        u = request.form['unit']
        c = request.form['comments']

        # if not title:
        #     flash('Title is required!')
        # elif not content:
        #     flash('Content is required!')
        # else:
        #     # messages.append({'title': title, 'content': content})
        #     write_data(title + content + t)
        #     return redirect(url_for('index'))
        write_data(date + cost + t + u + c)
        

    return render_template('create.html', types=types)


def write_data(s: str) -> None:
    with open("demofile2.txt", "a") as f:
        f.write(s)