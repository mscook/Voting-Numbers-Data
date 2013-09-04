# Copyright (C) Mitchell Stanton-Cook m.stantoncook@gmail.com
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import sys
import csv
import operator

seat = sys.argv[2].lower()

count_dict = {}
polls_dict   = {}

with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # Get the data for seat of interest
        if row[2].lower() == seat:
            poll_place_name = row[4].strip().replace(' ','_')
            poll_place_id   = int(row[3])
            cur_val = int(row[-2]) 
            polls_dict[poll_place_name] = poll_place_id
            # hhandle 1st instances otherwise append
            try:
                count_dict[poll_place_name] = (count_dict[poll_place_name]+
                                                            cur_val)
            except:
                count_dict[poll_place_name] = cur_val
# Sort dict in decreasing order
sorted_best = sorted(count_dict.iteritems(), 
                        key=operator.itemgetter(1), 
                        reverse=True)


# lets link to addresses
ids_dict = {}
with open('GeneralPollingPlacesDownload-15508.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for idx, row in enumerate(reader):
        if idx != 0:
            ids_dict[int(row[3])] = ' '.join(row[5:-2])

print "Rank, Polling Station Name, Voter Turnout, Address"
for idx, e in enumerate(sorted_best):
    print str(idx+1)+", "+e[0].replace('_', ' ')+", "+str(e[1])+", "+ids_dict[polls_dict[e[0]]]
