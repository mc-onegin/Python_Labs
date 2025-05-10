import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 1
B = 1
delta = 0
t = np.linspace(0, 2 * np.pi, 1000)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    frequency_ratio = (frame / 100, 1)
    x = A * np.sin(frequency_ratio[0] * t + delta)
    y = B * np.sin(frequency_ratio[1] * t)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init,
                    blit=True, interval=50)

plt.title('Анимация вращения фигуры Лисажу')
plt.grid()
plt.show()