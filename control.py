from flask import Flask, render_template, session, redirect, url_for
import valeez_main as valeez
import jinja2
import os

app = Flask(__name__)
app.secret_key = 'blahblahblah'

@app.route("/")
def index():
	city_dict = valeez.city_destination
	print city_dict
	return render_template("main.html", city_dict=city_dict)

if __name__ == "__main__":
	app.run(debug=True)