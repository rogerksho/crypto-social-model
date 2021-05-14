from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-1, 1, 20)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
