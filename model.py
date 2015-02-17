from flask import Flask, render_template, redirect, request, g, url_for, flash, make_response 
from flask import session as f_sess
import model
import jinja2
import os

app = Flask(__name__)
app.secret_key='thisissekrit123'
app.jinja_env.undefined = jinja2.StrictUndefined #this throws an error if a var is undefined

@app.route("/")
def index():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug = True)