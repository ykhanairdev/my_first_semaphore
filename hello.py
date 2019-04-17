from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello():
 return "Hello World! - This is my first Semaphore Build" + str(print_greeting())


@app.route("/yasser")
def hello():
 return "Hello World! - This is my first Semaphore Build" + str(print_greeting())





