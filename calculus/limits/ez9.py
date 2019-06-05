import matplotlib.pyplot as plt
from math import *

t = [i/10 for i in range(-100, 100)]
y = [2 + ((1/pi)*sin(i*pi)) for i in t]
p = 2 + ((1/pi)*sin(pi))
p2 = 2 + ((1/pi)*sin(2*pi))
p3 = 2 + ((1/pi)*sin(1.01*pi))

print(p3)

fig = plt.figure()
axes = fig.add_subplot(111)

axes.plot(t,y)
axes.plot(1,p, "r+")
axes.plot(2,p2, "r+")
axes.plot(1.01, p3, "g+")
plt.show()
print(y)
