import numpy as np
# import pandas as pd
import math
import matplotlib.pyplot as plt

## variable
savetofolder = "/home/ali/Documents/prwork/mathematics/"
savetofile   = "gaussian_quadratic1.png"


## Parameters
sigma = 2
mu    = 10
a,b,c = 1,2,1

## Functions
gaussian_distrib   = lambda x: (1/(sigma*math.sqrt(2*math.pi))) * math.e**((-0.5*((x-mu)/sigma)**2))
gaussian_quadratic = lambda x: math.e**((a*(x**2)) + (b*x) + c)






def generate_values(func, 
                    start =-10, 
                    stop  =10, 
                    step  =0.1,
                    label =f"a {a}, b {b}, c {c}"):
    print(func)
    x      = np.arange(start, stop, step)
    npfunc = np.vectorize(func) 
    y      = npfunc(x)

    plt.plot(x,y)
    plt.xlabel(label)
    plt.show()
    plt.savefig(f"{savetofolder}{savetofile}")



if __name__ == "__main__":
    generate_values(func=gaussian_quadratic, start=-1, stop=1)
