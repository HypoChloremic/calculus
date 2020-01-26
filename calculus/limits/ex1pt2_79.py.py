import math
import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('dark_background')

def f(x):
	#return x * math.sin(1/x)
	#return x**3
	return -x**2
	#return math.sin(x)

def g(x):
	#return -math.sqrt((x**3)**2)
	return 2 * x**2
def result(x_values, q):
	result = []
	for x in x_values:
		try:
			result.append(q(x))
		except ValueError as e:
			# the point here is to indicate that
			# the undefined roots, should be made visible
			# somehow
			result.append(10)
	result = np.array(result) 
	return result

x_values = np.arange(-10,10, 0.001)

plt.plot(x_values, result(x_values, f))
plt.plot(x_values, result(x_values, g))

plt.show()
