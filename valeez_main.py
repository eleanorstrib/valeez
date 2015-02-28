import json
import csv
import time
from datetime import datetime
import requests
import os

WUNDERGROUND_API_KEY = os.environ['WUNDERGROUND_API_KEY']
API_URL = "http://api.wunderground.com/api/"+WUNDERGROUND_API_KEY+"/forecast10day/q/"

city_destination = {
	"Boston, US" : ["MA/Boston"],
	"New York, US" : ["NY/New_York", "./static/img/newyork.jpg"],
	"Los Angeles, US" : ["CA/Los_Angeles"],
	"San Francisco, US" : ["CA/San_Francisco"],
	"Washington, DC" : ["DC/Washington"],
	"Berlin, DE" : ["Germany/Berlin"],
	"Cairo, EG" :["EG/Cairo"],
	"London, UK" : ["UK/London","./static/img/london.jpg"],
	"Mexico City, MX" : ["MX/mexico_city"],
	"Mumbai, IN" : ["IN/Mumbai"],
	"Paris, FR" : ["France/Paris", "/static/img/paris.jpg"],
	"Rio de Janeiro, BR" : ["BR/rio_de_janeiro"],
	"Rome, IT" : ["IT/Rome"],
	"Tokyo, JP" : ["JY/Tokyo"]
}

#lists and dictionaries the functions below will fill in
all_calendar_days = []
clothes_to_pack = {}

all_high_temps_f = []
all_low_temps_f = []
all_pop_pct = []
all_snow_in = []

# def today():
# 	today = datetime.date.today()
# 	today_date = today.day
# 	today_month = today.month
# 	return today_date, today_month

# today_date = control.depart_date_time.day
# today_month = control.depart_date_time.month

# def inputs(today_month, today_date):
# 	user_destination = control.get_packing(destination)
# 	user_destination_api = city_destination.get(user_destination)
# 	user_depart_date = control.get_packing(depart_date)
# 	user_return_date = control.get_packing(return_date)


# 	# user_depart_month = int(raw_input('what month are you leaving?'))



# 	user_number_days = control.num_days
# 	user_sex = control.get_packing(gender)
# 	user_biz = control.get_packing(trip_type)
# 	return user_destination_api, user_destination, user_depart_date, user_depart_month, user_number_days, user_sex, user_biz

# API_URL = "http://api.wunderground.com/api/ca5b10fb7297c6da/forecast10day/q/"

#this function figures out which calendar days I need to query the API for
def get_the_days(user_depart_month, user_number_days, user_depart_date):
	if user_depart_month == 2:
		for i in range (0, user_number_days):
			if user_depart_date++i <= 28:
				all_calendar_days.append(user_depart_date++i)
			else:
				all_calendar_days.append((user_depart_date++i)-28)
	if user_depart_month == 4 or user_depart_month == 6 or user_depart_month == 9 or user_depart_month == 11:
		for i in range (0, user_number_days):
			if user_depart_date++i <= 30:
				all_calendar_days.append(user_depart_date++i)
			else:
				all_calendar_days.append((user_depart_date++i)-30)
	if user_depart_month == 1 or user_depart_month == 3 or user_depart_month == 5 or user_depart_month == 7 or user_depart_month == 8 or user_depart_month == 10 or user_depart_month == 12:
		for i in range (0, user_number_days):
			if user_depart_date++i <= 31:
				all_calendar_days.append(user_depart_date++i)
			else:
				all_calendar_days.append((user_depart_date++i)-31)

	
	# print all_calendar_days
	return all_calendar_days

#this function calls the API and returns the forecasts for the days of the trip
def get_the_weather(all_calendar_days, user_destination_api):
	#these lists that will contain all of the high and low temps for the timeframe
	del all_high_temps_f[:]
	del all_low_temps_f[:]
	del all_pop_pct[:]
	r = requests.get("{}{}.json".format(API_URL, user_destination_api))
	j = r.json()
	

	if r.status_code == 200:
		for i in range (0,9):
			for day in all_calendar_days:
				if day == j['forecast']['simpleforecast']['forecastday'][i]['date']['day']:
					all_high_temps_f.append(int(j['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit']))
					all_low_temps_f.append(int(j['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit']))
					all_pop_pct.append(int(j['forecast']['simpleforecast']['forecastday'][i]['pop']))
					all_snow_in.append(j['forecast']['simpleforecast']['forecastday'][i]['snow_allday']['in'])
				else:
					continue
	else:
		all_high_temps_f.append('error')

	
	high_temp_f = max(all_high_temps_f)
	low_temp_f = min(all_low_temps_f)
	avg_pop = max(all_pop_pct)
	
	return (all_high_temps_f, all_low_temps_f, all_pop_pct, high_temp_f, low_temp_f, avg_pop)

def make_the_valeez(all_high_temps_f, all_pop_pct, user_sex, user_biz, user_number_days):
	avg_high_temps_f = sum(all_high_temps_f)/len(all_calendar_days)
	avg_low_temps_f = sum(all_low_temps_f)/len(all_calendar_days)
	max_pop_pct = max(all_pop_pct)
	max_snow_in = max(all_snow_in)
	with open('garment.csv', 'rU') as f:
			avg_high_temps_f = sum(all_high_temps_f)/len(all_calendar_days)
	avg_low_temps_f = sum(all_low_temps_f)/len(all_calendar_days)
	max_pop_pct = max(all_pop_pct)
	max_snow_in = max(all_snow_in)
	clothes_to_pack.clear()
	with open('garment.csv', 'rU') as f:
		reader = csv.reader(f)
		for row in reader:
			garments = row[0]
			
			if reader.line_num == 1:
				continue

			sex_column = row[1]
			if user_sex == 'female':
				sex_column = row[2]

			biz_column = row[5]
			if user_biz == 'casual':
				biz_column = row[6]
			if user_biz == 'vacation':
				biz_column = row[7]

			temp_column = row[12]
			if avg_high_temps_f <= 55 and avg_high_temps_f > 32:
				temp_column = row[13]
			if avg_high_temps_f <= 78 and avg_high_temps_f > 55:
				temp_column = row[14]
			if avg_high_temps_f <= 90 and avg_high_temps_f > 78:
				temp_column = row[15]
			if avg_high_temps_f >= 110:
				temp_column = row[16]

			layer_column = row[4]
			tbass_column = row[3]



			if sex_column =='True' and biz_column =='True' and temp_column =='True':
				if layer_column == '0' or layer_column == '1':
					clothes_to_pack[garments] = user_number_days
				if layer_column == '2':
					clothes_to_pack[garments] = user_number_days
				if layer_column == '3' and user_number_days > 2:
					clothes_to_pack[garments] = user_number_days/2
				else: 
					clothes_to_pack[garments] = user_number_days
				if layer_column == '4' or layer_column == '5':
					clothes_to_pack[garments] = 1


			rain_column = row[9]
			if max_pop_pct >= 40 and rain_column == 'True' and avg_high_temps_f >= 55:
				clothes_to_pack[garments] = 1

			clothes_to_pack_list = sorted([(value, key) for key, value in clothes_to_pack.iteritems()])
			
	return clothes_to_pack_list


def main():
	# inputs()
	# today_date, today_month = today()
	user_destination, user_destination_api, user_depart_date, user_depart_month, user_number_days, user_sex, user_biz = inputs(today_date, today_month)
	
	get_the_days(user_depart_month, user_number_days, user_depart_date)
	get_the_weather(all_calendar_days, user_destination)
	print "Here are all the high temperatures in Fahrenheit during your {} day trip to {} : {}.".format(user_number_days, user_destination, all_high_temps_f)
	print "Here are all the low temperatures in Fahrenheit during your {} day trip to {} : {}.".format(user_number_days, user_destination, all_low_temps_f)
	make_the_valeez(all_high_temps_f, all_pop_pct, user_sex, user_biz, user_number_days)





if __name__=="__main__":
	main()