"""
Helpful links:
https://flask.palletsprojects.com/en/2.0.x/quickstart/
https://hackersandslackers.com/flask-routes/
https://stackoverflow.com/questions/23846927/flask-unable-to-find-templates
https://stackoverflow.com/a/54381905
"""
#Import(s)
import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
DATABASE = 'database.db'
app.secret_key = os.urandom(12)

@app.route('/')
@app.route('/index.html')


def home():
    """
    Home page, also takes in date for display
    """
    return render_template('index.html', datetime = datetime.now())


@app.route('/page2.html')
def page2():
    """
    Second page, for Star Citizen info
    """
    return render_template('page2.html')


@app.route('/page3.html')
def page3():
    """
    Third page, for Bloodborne info
    """
    return render_template('page3.html')

if __name__ == '__main__':
    # Don't remove debug = true, https://stackoverflow.com/a/50146336
    app.run(debug = True)
