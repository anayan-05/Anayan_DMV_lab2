import numpy as np
import matplotlib.pyplot as plt
import time
plt.ion()
for i in range(50):
    plt.clf()
    data=np.random.randn(1000)
    plt.hist(data,bins=30)
    plt.draw()
    plt.pause(0.3)
plt.ioff()
plt.show()