#!/usr/bin/env python3

import csv
from datetime import datetime, timedelta
import re


cse_users = ['aaksoy', 'jakewheeler', 'lanle', 'simingl', 'earslan', 'ajanib', 'emhand', 'ayazdi']
with open('/Users/jakewheeler/Desktop/usage.csv', 'r', newline='') as input:
	with open('/Users/jakewheeler/Desktop/usage_final.csv', 'w') as output:
		input.readline()
		reader = csv.reader(input)
		writer = csv.writer(output, lineterminator='\n')
		total_elapsed = 0
		cse_elapsed = 0
		all = []
		for row in reader:
			endrow = []
			starttime = datetime.strptime(row[6], "%Y-%m-%dT%H:%M:%S")

			if "-" not in row[8]:
				row[8] = "0-" + row[8]
			time = re.split('-|:', row[8])
			delta = timedelta(days=int(time[0]), hours=int(time[1]), minutes=int(time[2]), seconds=int(time[3]))
			total_elapsed = total_elapsed + delta.total_seconds()
			if row[0] in cse_users:
				cse_elapsed = cse_elapsed + delta.total_seconds()
			endrow.append(starttime)
			endrow.append(total_elapsed)
			endrow.append(cse_elapsed)
			all.append(endrow)
		writer.writerows(all)
