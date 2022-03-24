# HelloRoute.py
from flask import Flask
app = Flask(__name__)

# Option #1: using @app.route() decorator.
@app.route('/hello')
def hello_world():
    return "Hello World"

# # Option #2: using app.add_url_rule() function.
# def hello_world():
#    return "hello world"
# app.add_url_rule("/", "hello", hello_world)

if __name__ == '__main__':
    #app.debug = True
    app.run()
