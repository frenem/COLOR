
# A very simple Flask Hello World app for you to get started with...

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<color>')
def home(color=None):
    return render_template('home.html',color=color)
