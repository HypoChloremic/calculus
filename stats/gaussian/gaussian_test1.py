import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

## variable
savetofolder = "/home/ali/Documents/prwork/mathematics"
savetofile   = "gaussian_distrib2.png"

sigma = 2
mu    = 10


x    = np.arange(-10,10, step=0.01)
func   = lambda x: (1/(sigma*math.sqrt(2*math.pi))) * math.e**((-0.5*((x-mu)/sigma)**2))
npfunc = np.vectorize(func) 

y = (1/(sigma*math.sqrt(2*math.pi))) * math.e**((-0.5*((x-mu)/sigma))**2)
y2 = npfunc(x)
# print(y, x)

plt.plot(x,y2)
plt.xlabel(f"mu {mu}, sigma {sigma}")
plt.show()
plt.savefig(f"{savetofolder}/{savetofile}")
