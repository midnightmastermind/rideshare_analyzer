import csv
from datetime import datetime
from pprint import pprint


day_lookup_value = input("What day of the week do you want the average of? ")
time_lookup_value = input("What time? ")

price_total_value =
trip_total_value =

with open('./lyft.csv') as csv_file:
	csv_reader = csv.reader(csv_file, quotechar="'", delimiter=',')

	price_column = 1
	datetime_column = 0

	for row in csv_reader:
		datetime_value = datetime.strptime(row[datetime_column], "%A, %B %d, %Y %H:%M %p")
