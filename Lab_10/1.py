
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 400)
plt.figure(figsize=(10, 6))
for n in range(1, 8):
    Pn = legendre(n)
    plt.plot(x, Pn(x), label=f'n = {n}')
plt.title('Полиномы Лежандра')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend(title='Степень полинома')
plt.show()