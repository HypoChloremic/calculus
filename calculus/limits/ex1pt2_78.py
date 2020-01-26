import math
import matplotlib.pyplot as plt 
import numpy as np

def f(x):
	#return x * math.sin(1/x)
	return math.sin(1/x)
	#return math.sin(x)

x_values = np.arange(-10,10, 0.001)
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
