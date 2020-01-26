import math
import matplotlib.pyplot as plt 
import numpy as np

def f(x):
	return math.sqrt(x**3 - x)

x_values = np.arange(-10,10, 0.1)
print(x_values)

result = []
for x in x_values:
	try:
		result.append(f(x))
	except ValueError as e:
		# the point here is to indicate that
		# the undefined roots, should be made visible
		# somehow
		result.append(10)
result = np.array(result) 

plt.plot(x_values, result)
plt.show()
