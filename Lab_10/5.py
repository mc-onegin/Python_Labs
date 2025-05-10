import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def local_mse(x, y):
    return (x - y)**2

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = local_mse(X, Y)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Local MSE')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z + 1e-5, cmap='plasma')
ax2.set_title('Local MSE log')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(MSE)')
ax2.set_zscale('log')

plt.tight_layout()
plt.show()