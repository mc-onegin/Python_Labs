import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

t = np.linspace(0, 2 * np.pi, 1000)

A1_init = 1.0
f1_init = 1.0
A2_init = 1.0
f2_init = 1.0

def update(val):
    A1 = slider_A1.val
    f1 = slider_f1.val
    A2 = slider_A2.val
    f2 = slider_f2.val

    wave1.set_ydata(A1 * np.sin(f1 * t))
    wave2.set_ydata(A2 * np.sin(f2 * t))
    combined_wave.set_ydata(wave1.get_ydata() + wave2.get_ydata())

    ax_wave1.relim()
    ax_wave1.autoscale_view()

    ax_wave2.relim()
    ax_wave2.autoscale_view()

    ax_combined.relim()
    ax_combined.autoscale_view()

    fig.canvas.draw_idle()

fig, (ax_wave1, ax_wave2, ax_combined) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
plt.subplots_adjust(left=0.15, right=0.85, hspace=0.4)

ax_wave1.set_title('Первая волна')
ax_wave2.set_title('Вторая волна')
ax_combined.set_title('Сложение волн')

wave1, = ax_wave1.plot(t, A1_init * np.sin(f1_init * t), label='Волна 1', color='blue')
wave2, = ax_wave2.plot(t, A2_init * np.sin(f2_init * t), label='Волна 2', color='orange')
combined_wave, = ax_combined.plot(t, wave1.get_ydata() + wave2.get_ydata(), label='Сложенная волна', color='green')

ax_wave1.legend()
ax_wave2.legend()
ax_combined.legend()

ax_A1 = plt.axes([0.15, 0.01, 0.65, 0.03])
slider_A1 = Slider(ax_A1, 'Амплитуда Волны 1', 0.01, 5.0, valinit=A1_init)

ax_f1 = plt.axes([0.15, 0.05, 0.65, 0.03])
slider_f1 = Slider(ax_f1, 'Частота Волны 1', 0.01, 10.0, valinit=f1_init)

ax_A2 = plt.axes([0.15, 0.09, 0.65, 0.03])
slider_A2 = Slider(ax_A2, 'Амплитуда Волны 2', 0.01, 5.0, valinit=A2_init)

ax_f2 = plt.axes([0.15, 0.13, 0.65, 0.03])
slider_f2 = Slider(ax_f2, 'Частота Волны 2', 0.01, 10.0, valinit=f2_init)

slider_A1.on_changed(update)
slider_f1.on_changed(update)
slider_A2.on_changed(update)
slider_f2.on_changed(update)

plt.show()