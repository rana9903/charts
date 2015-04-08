import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.pyplot as plt

print "hello"

# a = np.array([[1,4,5], [4, 5, 6], [7, 8, 9]],float)

# 	# np.array([[1,4,5,8],[4, 5, 6]],float)
# 	# np.array([[1, 2, 3], [4, 5, 6]], float) 

# print a
# print a.mean()
# print a.var()
# print a.std()
# print a.max()

# print a[0,0]
# print a [:,2]
# print a.shape
# print a.dtype

# a = np.array([1,2,3,4,5,6])
# print np.median(a)

# b = np.array (range (10))
# print np.zeros((10,10))
# print (a[2:])



from pylab import *

# ax = axes([0.025,0.025,0.95,0.95])

# ax.set_xlim(0,4)
# ax.set_ylim(0,3)
# ax.xaxis.set_major_locator(MultipleLocator(1.0))
# ax.xaxis.set_minor_locator(MultipleLocator(0.1))
# ax.yaxis.set_major_locator(MultipleLocator(1.0))
# ax.yaxis.set_minor_locator(MultipleLocator(0.1))
# ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
# ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
# ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
# ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
# ax.set_xticklabels([])
# ax.set_yticklabels([])

# # savefig('../figures/grid_ex.png',dpi=48)
# show()
a = np.arange(10)
print a
print a[2:9:3]
print a[-4:]
print a[::2]



# fig = plt.figure()
# ax = fig.add_subplot(111)

# ## the data
# N = 5
# menMeans = [18, 35, 30, 35, 27]
# menStd =   [2, 3, 4, 1, 2]
# womenMeans = [25, 32, 34, 20, 25]
# womenStd =   [3, 5, 2, 3, 3]

# ## necessary variables
# ind = np.arange(N)                # the x locations for the groups
# width = 0.35                      # the width of the bars

# ## the bars
# rects1 = ax.bar(ind, menMeans,color='black')

# rects2 = ax.bar(ind+width, womenMeans, width,
#                     color='red',
#                     yerr=womenStd,
#                     error_kw=dict(elinewidth=2,ecolor='black'))

# axes and labels
# ax.set_xlim(-width,len(ind)+width)
# ax.set_ylim(0,45)
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# xTickMarks = ['Group'+str(i) for i in range(1,6)]
# ax.set_xticks(ind+width)
# xtickNames = ax.set_xticklabels(xTickMarks)
# plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
# ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

# plt.show()
