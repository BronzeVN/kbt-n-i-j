import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-40, 40)
ax.set_ylim(-30, 30)

heart, = ax.plot([], [], 'r')

def init():
    heart.set_data([], [])
    return heart,

def update(frame):
    t = np.linspace(0, 2*np.pi, 100)
    x = 20 * np.sin(t)**3
    y = 15 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    heart.set_data(x * (1 + 0.005 * frame), y * (1 + 0.005 * frame))  # Scale the heart with frame
    return heart,

ani = FuncAnimation(fig, update, frames=range(90), init_func=init, blit=True, interval=50)
plt.axis('off')
plt.show()
