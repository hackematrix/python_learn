import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


plt.rcParams['toolbar'] = 'None'
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(-1, 1, 0.05)
Y = np.arange(-1, 1, 0.05)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X**2)+np.cos(X**2)

ax.plot_surface(X, Y, Z, linewidth=0, cmap=cm.coolwarm)
plt.show()
