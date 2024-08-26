import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
for i in range(1,5):
    plt.plot(x,x**i)
plt.show()