
import datetime
import numpy as np
import matplotlib.colors as colors
import matplotlib.finance as finance
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

startdate = datetime.date(2014,1,1)
today = enddate = datetime.date.today()
ticker = 'SU.TO'

fh = finance.fetch_historical_yahoo(ticker, startdate, enddate)
r = mlab.csv2rec(fh); fh.close()
r.sort()

print r.open
print len (r.open)

textsize = 9
left, width = 0.1, 0.8
rect1 = [left, 0.7, width, 0.2]

fig = plt.figure(facecolor='white')
axescolor  = '#f6f6f6'  # the axes background color
ax1 = fig.add_axes(rect1, axisbg=axescolor)  #left, bottom, width, height
ax1.plot(r.date, r.open, color='darkgoldenrod')  
ax1.set_title('%s daily'%ticker)
plt.grid(True)
plt.show()


