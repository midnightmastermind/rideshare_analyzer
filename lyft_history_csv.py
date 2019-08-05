import csv
from datetime import datetime
from pprint import pprint

values = []


with open('./lyft.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
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
				values.append([datetime_value.strftime("%A, %B %d, %Y %H:%M %p"), price])

		line_count = line_count + 1

with open('./final.csv') as csv_file:
	csv_reader = csv.reader(csv_file, quotechar="'", delimiter=',')

	total_column = 1
	datetime_column = 0

	for row in csv_reader:
		datetime_value = datetime.strptime(row[datetime_column], "%A, %B %d, %Y %I:%M %p")
		datetime_value = datetime_value.strftime("%A, %B %d, %Y %I:%M %p")
		print(row[total_column])
		price = float(row[total_column].replace('$',''))
		values.append([datetime_value, price])

pprint(values)
with open('uber_lift_trip_data.csv', 'w', newline='') as csvfile:
	for value in values:
		writer = csv.writer(csvfile, delimiter=',',
                        quotechar="'", quoting=csv.QUOTE_MINIMAL)
		writer.writerow(value)
