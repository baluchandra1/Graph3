'''Graph plotting code for discontinuous functions.
XY plot
X axis range in integers'''




import matplotlib.pyplot as plt
#from matplotlib import rc
from matplotlib.ticker import MultipleLocator
import numpy as np


#################SAMPLE SPACE#######################
fig, ax = plt.subplots()
######Function Range############
xrange = [-10, 10]
yrange = [-5, 5]
x = np.linspace(xrange[0], xrange[1], 200000)
plt.axhline(y = 0, color = 'k', linestyle = '-')
plt.axvline(x = 0, color = 'k', linestyle = '-')

###########DISCONTINUOUS FUNCTIONS###############
def df(k):
    y = abs(k)/k
    y[:-1][np.diff(y) >= 0.5] = np.nan
    return y


##########Function###########
function = [[df(x), r'$\frac{|x|}{x}$'] ]
#function_label = ['$y=x^2$', '$y=x^3$']

def fctn(function, xrange):
    i = len(function)
    #x = np.linspace(xrange[0], xrange[1], 200000)
    for y in function:
        x = np.linspace(xrange[0], xrange[1], 200000)
        ax.plot(x, y[0],label = y[1])

        plt.legend()

        #print(y)
    return plt.show()
plt.grid()
plt.ylim(yrange[0], yrange[1])
ax.set(xlabel='x-axis', ylabel='y-axis',
       title='')
fctn(function,xrange)
