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
	city_clean = str([key for key, value in city_dict.items() if value[0] == city])
	city_clean = city_clean.translate(None, "[]'")
	# dates
	depart_date = request.args.get("depart_date")
	depart_date_time = datetime.strptime(depart_date, "%m/%d/%Y")
	user_depart_month = depart_date_time.month
	user_depart_date = depart_date_time.day
	return_date = request.args.get("return_date")
	return_date_time = datetime.strptime(return_date, "%m/%d/%Y")
	user_number_days = (return_date_time-depart_date_time).days
	#other variables
	trip_type = request.args.get("trip_type")
	gender = request.args.get("gender")
	#running functions from main file
	get_days = valeez.get_the_days(user_depart_month, user_number_days, user_depart_date)
	print get_days
	get_the_weather = valeez.get_the_weather(get_days, city)
	print get_the_weather, "get the weather"
	make_the_valeez = valeez.make_the_valeez(get_the_weather[0], get_the_weather[1], gender, trip_type, user_number_days)
	print make_the_valeez

	return render_template("hello.html", city = city,
		 depart_date=depart_date, return_date = return_date, 
		 user_number_days = user_number_days, trip_type = trip_type, 
		 city_clean = city_clean, get_the_weather=get_the_weather, 
		 make_the_valeez=make_the_valeez)

if __name__ == "__main__":
	app.run(debug=True)