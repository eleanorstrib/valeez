from flask import Flask, render_template, session, redirect, request, url_for
import valeez_main as valeez
from datetime import date, datetime
import jinja2
import os

app = Flask(__name__)
app.secret_key = 'blahblahblah'


@app.route('/')
def index():
	city_dict = valeez.city_destination
	return render_template("main.html", city_dict=city_dict)

@app.route("/getpacking")
def get_packing():
	#destination
	city = request.args.get("city")
	print city
	city_dict = valeez.city_destination
	print city_dict
	city_clean = str([key for key, value in city_dict.items() if value[0] == city])
	
	print city_clean
	# dates
	depart_date = request.args.get("depart_date")
	depart_date_time = datetime.strptime(depart_date, "%m/%d/%Y")
	return_date = request.args.get("return_date")
	return_date_time = datetime.strptime(return_date, "%m/%d/%Y")
	num_days = (return_date_time-depart_date_time).days
	#other variables
	trip_type = request.args.get("trip_type")
	gender = request.args.get("gender")

	return render_template("hello.html", city = city,
		 depart_date=depart_date, return_date = return_date, 
		 num_days = num_days, trip_type = trip_type, city_clean = city_clean)

if __name__ == "__main__":
	app.run(debug=True)