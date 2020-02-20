import math
import matplotlib.pyplot as plt
import numpy as np

## Save folders and locations
savetofolder = "/home/ali/Documents/prwork/mathematics/"
savetofile   = "factorial.png"


genFact = lambda x: math.factorial(x)

x = np.arange(0,8)
x2 = np.array([1,2])
y = np.vectorize(genFact)(x)

plt.title("(x, x!)")

plt.scatter(x,y, s=4)
#plt.show()
plt.savefig(savetofolder + savetofile)

 
