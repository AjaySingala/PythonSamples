# template_simple.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("template_simple.html")

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('template_simple.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)
