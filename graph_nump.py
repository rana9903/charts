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
import math
import re
from pylab import *
# import matplotlib.pyplot as *
from balloontip import WindowsBalloonTip
import matplotlib.finance as finance
import numpy as np

"""
sample usage:
>>> import ystockquote
>>> print ystockquote.get_price('GOOG')
529.46
"""
symbol_all = ['XEG.TO', 'CNQ.TO', 'SU.TO','CPG.TO','NOK','F', 'BB.TO', 'XGD.TO','AGI.TO','THI.TO']
# symbol_oil = ['XEG.TO', 'CNQ.TO', 'SU.TO', 'CPG.TO']
symbol_oil = ['XEG.TO']
symbol_us = ['F','NOK','FB','BB.TO']

# symbol = ['THI.TO','XEG.TO']
data = []
today =time.strftime("%Y%m%d")
fromDate="20140101" 

startdate = datetime.date(2014,1,1)
today = enddate = datetime.date.today()
ticker = 'SU.TO'




def filldata(stock_symbol):
    global data
    # a numpy record array with fields: date, open, high, low, close, volume, adj_close)
    fh = finance.fetch_historical_yahoo(stock_symbol, startdate, enddate)
    r = mlab.csv2rec(fh); fh.close()
    r.sort()
    # print r[1]["high"]
    # print r["high"][2]
    # # print np.mean(r["high"])


    # for 
    # print 
    # print r.shape[1]
        # print r["high"][9:-1]

    end = r.shape[0]    
    arr = np.zeros((end,), dtype=[('var1','f8'),('var2','f8')])
    print arr
    print arr["var2"]
    # print arr["var1"]
    print type(r) 
    end = r.shape[0]
    # avghigh = np.zeros(((end+1),1))
    # print avghigh
   
    partision = r[end-10:end]
    print np.mean(partision["high"])
    print np.mean(partision["low"])
    print np.mean(partision["close"])
    print np.mean(partision["volume"])
    
    # x = np.zeros((2,),dtype=('i4,f4,a10'))
    # print x
    # x[:] = [(1,2.,'Hello'),(2,3.,"World")]
    # print x[1]

    # print x

    p = np.append(r, arr, 1)
    # # p = np.array([[1,2],[3,4]])
    # q = np.zeros((p.shape[0],3)) 
    # print p
    # print q
    # p = np.append(p, q, 1)
    # print p
    # np.append(r,avghigh, axis = 0) 
    # np.column_stack(data, avghigh)
    # np.column_stack((r, zeros(shape(r)[0])))

        # r.insert(np.mean(partision["high"]))
    # print r


    # print np.mean( r["high"][end-10:end])
    # print np.mean( r["high"][-10:])
    # print len( r["open"])
    # print min ( r["open"])
    # print max (r["close"])
    # print r ["close"]

# # Get historical data 
#     data = get_historical_prices(stock_symbol, fromDate, today)
#     #Adding Extra Columns 
#     data[0].append("Average High") 
#     data[0].append("Average Low") 
#     data[0].append("Action") 
#     """
#     Updating the list with todays Data
#     """
#     if (time.strftime("%Y-%m-%d") not in data[1][0]):
#         today_data= get_all(stock_symbol)
#         data.insert(1,[])
#         data[1].append(time.strftime("%Y-%m-%d"))
#         data[1].append(today_data['open'])
#         data[1].append(today_data['days_high'])
#         data[1].append(today_data['days_low'])
#         data[1].append(today_data['last_price'])
#         data[1].append(today_data['volume'])
#         data[1].append(today_data['adj_close'])
    
    
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
"""
Adding last 10 days average high
Adding Bull vs Bear in graph
"""
def addavgHighandLow():
    global data
    start =1
    end = 10
    while (start+11)<len(data):
        datseg = data[start:(start+end)]
        data[start].append(averagehigh(datseg)) 
        data[start].append(averagelow(datseg)) 
        # data[start].append(averagelow(datseg))
        if float(data[start][3]) > float(data[start][7]):
            data[start].append("BULL")
        elif float(data[start][2]) < float(data[start][8]): 
            data[start].append("BEAR")  
        else:
            data[start].append("----")
        start +=1

# data.append(get_all("SU.TO"))
# Printing the results 
def printData():
    global data
    print "-" * 120 
    for row in data:
        if len(row)>9:
            print "{0:^10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>15} {6:>15} {7:>10} {8:>10} {9:>10}".\
                format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),str(row[4]),\
                str(row[7]), str(row[8]), str(row[6]), str(row[5]), str(row[9]))
            # print "{0:^10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>15} {6:>15}".\
            #     format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),str(row[4]),\
            #     str(row[5]), str(row[9]))
        # if "Date" in row[0]:
        #     print "-" * 120 

# Drawing the plot
def drawPlot(plotdata,ticker):
    global data
    high=[]
    low =[]
    avghigh=[]
    avglow =[]
    closing =[]
    volume =[]
    x =[]
    i =0;
    for row in plotdata:
        # print row 
        if len(row)>9 and ("Date" not in row[0]):
            high.append(float (row[2]))
            low.append(float (row[3]))
            avghigh.append(float(row[7]))
            avglow.append(float(row[8]))
            closing.append(float(row[4]))
            volume.append(row[5])
            i+=1
            x.append(i) 
    high.reverse()
    low.reverse()
    avghigh.reverse()
    avglow.reverse()
    closing.reverse()
    
    fig = plt.figure()
    

    ax1 = fig.add_axes([0.05, 0.05, 0.9, 0.9])  # left, bottom, width, height (range 0 to 1)
    # ax2 =  fig.add_axes([0.05,0.05,.9,.2]
    ax1.plot(x, high,'g:o', x, low,'r-o', x,avghigh,'k-o', x, avglow,'k-o', x, closing, 'b--o',linewidth=2.0)
    ax1.set_title(ticker)
    ax1.yaxis.tick_right()
    # ax1.set_yticklabels(np.arange(min(low)-1, max(high)+1, 0.05))
    ax1.set_xlim(0,i+1)
    ax1.set_ylim(min(low)-.01, max(high)+0.1)
    ax1.xaxis.set_major_locator(MultipleLocator(5.0))
    ax1.xaxis.set_minor_locator(MultipleLocator(1))
    ax1.yaxis.set_major_locator(MultipleLocator(min(avglow)/100))
    ax1.yaxis.set_minor_locator(MultipleLocator(min(avglow)/500))
    ax1.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax1.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    ax1.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax1.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    
    
 

    # ax = pl.subplot(111)
    # rects1 = ax = pl.subplot(111).bar(i, volume,color='black', width=1)

    # ax1.set_yticklabels(np.arange(min(low), max (high)+1,0.05))
    # ax.set_xticklabels(np.arange(0, i+1, 1.0))
    # plt.figure()
    # plt.subplot(211)
    # plt.plot(x, high,'g-o', x, low,'r-o', x,avghigh,'k-o', x, avglow,'k-o', x, closing, 'b--o',linewidth=2.0)
    # plt.xticks(np.arange(0, i+1, 1.0))
    # plt.yticks (np.arange(min(low), max (high)+1,0.10))
    # # plt.xaxis.set_major_locator(MultipleLocator(5.0))

    # # plt.plot(x,avghigh,'ko')
    # # # plt.plot(x, closing, 'bo')
    # # plt.plot(x, high, 'go')
    # # plt.plot(x, low, 'ro')
    # plt.grid(True)
    # plt.suptitle(ticker, fontsize=20)
    # # plt.subplot(212)
    # # plt.plot(x,volume, 'g-o')
    # # plt.grid(True)
    show()

for ticker in symbol_oil:
    filldata(ticker)
    # addavgHighandLow()
    # printData()
    # drawPlot(data, ticker)
