import numpy as np
import matplotlib.pyplot as plt

def lisajous_curve(A, B, delta, frequency_ratio, t):
    x = A * np.sin(frequency_ratio[0] * t + delta)
    y = B * np.sin(frequency_ratio[1] * t)
    return x, y
A = 1
B = 1
delta = np.pi / 2
t = np.linspace(0, 2 * np.pi, 1000)
frequency_ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
plt.figure(figsize=(12, 10))
for i, ratio in enumerate(frequency_ratios):
    plt.subplot(2, 2, i + 1)
    x, y = lisajous_curve(A, B, delta, ratio, t)
    plt.plot(x, y)
    plt.title(f'Фигура Лисажу: {ratio[0]}:{ratio[1]}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.grid()

plt.suptitle('Фигуры Лисажу', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()