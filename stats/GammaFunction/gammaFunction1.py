import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math
import seaborn

## save to
savetofolder = "/home/ali/Documents/prwork/mathematics/"
savetofile   = "gammafunction_nointegral_1.png"



z = 2

# This is the Gamma function 
# but without the integral
# i.e. it is the core function
gamma = lambda x: (x**(z-1))*(math.e**(-x))


x = np.arange(-1,10, 0.1)
y = np.vectorize(gamma)(x)


'''the seaborn.set() method
will set the style of the figure
to classic seaborn, however not 
directly visible honestly

the seaborn.set_style("ticks")
puts ticks on the spines of the 
axis. 
'''

seaborn.set()
seaborn.set_style("ticks")


ax=seaborn.lineplot(x,y)

'''
ax.fill_between(x,y) will fill
the area under the curve, when we feed
it the x,y. 

ax.axhline(0) will draw a line 
with given style at the y-coordinate
0
'''
ax.fill_between(x,y, color="orange")
ax.axhline(0, ls="--")
ax.axvline(0, ls="--")

#ax.grid(True)
#seaborn.despine(x,y)
#

#plt.show()
plt.savefig(savetofolder + savetofile)
