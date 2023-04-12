import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

i = 0
x = list()
y = list()

while i < 100:
    plt.axis([0, 100, 0, 1])
    temp_y = np.random.random()
    x.append(i)
    y.append(temp_y)
    plt.scatter(i, temp_y)
    i += 1
    plt.show()
    plt.pause(0.01)
    plt.clf()
