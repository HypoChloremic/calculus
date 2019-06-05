import matplotlib.pyplot as plt

a = [t for t in range(-10, 10)]
b = [4.9*t**2 for t in a]

bDelta= [9.8*t for t in a]

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(a,b, "r")
axes.plot(a,bDelta, "b")

plt.show()