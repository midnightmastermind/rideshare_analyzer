import csv
from datetime import datetime
from pprint import pprint
import glob
from terminaltables import DoubleTable

#
path = './statement*.csv'

files = glob.glob(path)
values = []

for file in files:
	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, quotechar='"', delimiter=',')
		line_count = 0
		trip_datetime_column = None
		trip_total_price_column = None

		for row in csv_reader:
			if line_count == 0:
				datetime_column = row.index("Date/Time")
				total_price_column = row.index("Total")
			else:
				datetime_value = datetime.strptime(row[datetime_column], "%A, %B %d, %Y %I:%M %p")
				datetime_value = datetime_value.strftime("%A, %B %d, %Y %I:%M %p")
				total_price = float(row[total_price_column].replace('$',''))
				values.append([datetime_value, total_price])

			line_count += 1

with open('./lyft.csv') as csv_file:
	csv_reader = csv.reader(csv_file, quotechar='"', delimiter=',')
	line_count = 0
	price_column = 1
	time_column = 0
	date_column = 2

	for row in csv_reader:
		if line_count != 0:
			if row[price_column]:
				price = eval(row[price_column].replace('$',''))

				date = row[date_column]
				time = row[time_column]

				datetime_value = datetime.strptime(date + ' ' + time, "%a, %b %d, %Y %I:%M %p")
				datetime_value = datetime_value.strftime("%A, %B %d, %Y %I:%M %p")
  mm
				values.append([datetime_value, price])

		line_count = line_count + 1

# def sortSecond(val):
#     return val[0]
#
# headers = ["Date/Time", "Amount"]
# values.sort(key = sortSecond)
# values.insert(0, headers)
# print(table.table))



# table = DoubleTable(values, 'title=Rideshare Data')
# print(table.table)
# pprint(values)

# with open('uber_lift_trip_data.csv', 'w', newline='') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=',',
# 					quotechar="'", quoting=csv.QUOTE_MINIMAL)
# 	writer.writerow(["Date/Time", "Amount"])
# 	for value in values:
# 		writer.writerow(value)

# current_day = int(input("What day of the week do you want the average of? "))
# current_hour = int(input("What time? "))

days = []
price_total_value = 0
trip_total_value = 0
final_prices = []

for hour in range(0,24):
	final_prices.append([datetime.strptime(str(hour), '%H').strftime('%I %p')])
	for weekday in range(0,7):
		price_total_value = 0
		trip_total_value = 0
		avg_value = 0
		for value in values:
			datetime_value = datetime.strptime(value[0], "%A, %B %d, %Y %I:%M %p")
			if datetime_value.weekday() == weekday and datetime_value.hour == hour:
				price_amount = float(value[1])
				current_daytime = datetime_value.strftime("%B %d")

				if [current_daytime, datetime_value.hour] not in days:
					days.append([current_daytime, datetime_value.hour])
					trip_total_value += 1

				price_total_value += price_amount
		if trip_total_value != 0:
			avg_value = '${:,.2f}'.format(price_total_value / trip_total_value)
		else:
			avg_value = "Not Driven"

		final_prices[hour].append(avg_value)

headers = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
final_prices.insert(0, headers)
# print(table.table))
table = DoubleTable(final_prices, 'title=Rideshare Data')
print(table.table)


	# current_day = datetime.now().weekday()
	# current_hour = datetime.now().hour
	#
	# if current_hour == 0:
	# 	current_hour = 12
	# if current_hour > 12:
	# 	current_hour -= 12

	# if datetime_value.hour == current_hour and datetime_value.weekday() == current_day:
	# 	price_total_value += price_amount

# 	current_daytime = datetime_value.strftime("%B %d")
#
# 	if current_daytime not in days:
# 		days.append([current_daytime, datetime_value.hour])
# 		current_day[datetime_value.day][datetime_value.hour][1] += 1
# 		# trip_total_value += 1
# 	current_day[datetime_value.day][datetime_value.hour][0] += price
#
# # if trip_total_value != 0:
# # 	price_avg = price_total_value / trip_total_value
# # else:
# # 	price_avg = 0
#
#
# final_table = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
#
# for i in range(len(current_day)):
# 	for j in range(len(current_day[i])):
# 		if current_day[i][j][1] != 0:
# 			final_table[i][j+1] = '$' + str(round(current_day[i][j][0] / current_day[i][j][1],2))
#
# table = AsciiTable(final_table)
# print(table.table)
#
# # if price_avg > 18:
# # 	print('Go Drive!')
# # elif price_avg == 0:
# # 	print('Never Driven')
# # else:
# # 	print('Hold Up')
