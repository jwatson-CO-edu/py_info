import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure(figsize=(9, 9), dpi=100)
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#np.linspace(-2, 2, 100)
r = [0]#z**2 + 1
x = [0,0,0,0,0]#r * np.sin(theta)
y = [0,0,2,2,0]#r * np.cos(theta)
z = [0,2,2,0,0]
ax.plot(x, y, z)
ax.legend()

plt.show()