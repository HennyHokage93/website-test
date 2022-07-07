# Jahquan Thomas
# SDEV 300
# Lab 6
# 06/25/22

"""System Module."""
from datetime import date
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index_qh.html')
def home():
    """Displays the homepage for the website."""
    return render_template('index_qh.html', date=date.today())


@app.route('/page2_qh.html')
def page2():
    """Pathway for page 2 on webpage."""
    return render_template('page2_qh.html', date=date.today())


@app.route('/page3_qh.html')
def page3():
    """Pathway for page 3 on webpage."""
    return render_template('page3_qh.html', date=date.today())


@app.route('/new_user_form.html')
def user_register():
    """Pathway for user registration form."""
    return render_template('new_user_form.html', date=date.today())


if __name__ == '__main__':

    app.run(debug=True)
