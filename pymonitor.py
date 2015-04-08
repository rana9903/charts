#!/usr/bin/env python
#
#  Copyright (c) 2007-2008, Corey Goldberg (corey@goldb.org)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
from ystock import *
import time
import datetime
import re
import matplotlib.pyplot as plt

"""
sample usage:
>>> import ystockquote
>>> print ystockquote.get_price('GOOG')
529.46
"""

symbol = ['XEG.TO', 'CNQ.TO', 'SU.TO','GOOG','F', 'FB']
stock_sybol="SU.TO"
today =time.strftime("%Y%m%d")
fromDate="20140101"

# Get todays data and add it to the Data
data = get_historical_prices(stock_sybol, fromDate, today)
data[0].append("Average High") 
data[0].append("Average Low") 
data[0].append("Action") 
data[0].append("Action") 
# Updating the list with todays Data
today_data= get_all(stock_sybol)

data.insert(1,[])
data[1].append(time.strftime("%Y-%m-%d"))
data[1].append(today_data['open'])
data[1].append(today_data['days_high'])
data[1].append(today_data['days_low'])
data[1].append(today_data['last_price'])
data[1].append(today_data['volume'])
data[1].append(today_data['adj_close'])

#Calculating Average High
def averagehigh(average):
    averagehigh=0
    for listitem in average:
        if listitem[0] != "Date":
            averagehigh = averagehigh+ float (listitem[2])
    return  "{0:10.3f}".format(float(averagehigh/len(average)))

#Calculating Average Low
def averagelow(average):
    averagelow=0
    for listitem in average:
        if listitem[0] != "Date":
            averagelow = averagelow+ float (listitem[3])
    return "{0:10.3f}".format(float(averagelow/len(average)))

# Adding last 10 days average high
start =1
end = 10
while (start+11)<len(data):
    datseg = data[start:(start+end)]
    data[start].append(averagehigh(datseg)) 
    data[start].append(averagelow(datseg)) 
    
    if float(data[start][3]) > float(data[start][7]):
        data[start].append("BULL")
    elif float(data[start][2]) < float(data[start][8]): 
        data[start].append("BEAR")  
    else:
        data[start].append("----")
    start +=1

# data.append(get_all("SU.TO"))
# Printing the results 
print "-" * 120 
for row in data:
    if len(row)>9:
        print "{0:^10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>15} {6:>15} {7:>10} {8:>10} {9:>10}".\
            format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),str(row[4]),\
            str(row[7]), str(row[8]), str(row[6]), str(row[5]), str(row[9]))
        # print "{0:^10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>15} {6:>15}".\
        #     format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),str(row[4]),\
        #     str(row[5]), str(row[9]))
    if "Date" in row[0]:
        print "-" * 120 
