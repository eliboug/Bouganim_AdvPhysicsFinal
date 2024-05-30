import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# inputs
u0 = 0.1749  
t0 = 36.176  # time of maximum alignment
tE = 152.1   # Einstein crossing time

# Time array over which I will calculate the magnification
time = np.linspace(t0 - 3 * tE, t0 + 3 * tE, 500)  # Span centered at t0

# lens-source separation equation
def u(t, u0, t0, tE):
    return np.sqrt(u0**2 + ((t - t0) / tE)**2)

# magnification equation A(t)
def magnification(t, u0, t0, tE):
    u_t = u(t, u0, t0, tE)
    return (u_t**2 + 2) / (u_t * np.sqrt(u_t**2 + 4))

# calculate the magnification for each time point
mag = magnification(time, u0, t0, tE)

# set up the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# line setup for the plots
line1, = ax1.plot([], [], 'ro-', label='Source-Lens System')
line2, = ax2.plot([], [], 'b-', label='Microlensing Light Curve')

# graph 1 settings
ax1.set_xlim(time[0], time[-1])  
ax1.set_ylim(0, max(u(time, u0, t0, tE)) + 0.1)  # Slightly above max u to keep the dot in view
ax1.set_title('Relative Motion of Source and Lens')
ax1.set_xlabel('Time (days)')
ax1.set_ylabel('Relative Y Position (Einstein Radii)')
ax1.grid(True)

# graph 2 settings
ax2.set_xlim(time[0], time[-1])
ax2.set_ylim(1, max(mag) + 0.5)
ax2.set_title('Microlensing Light Curve')
ax2.set_xlabel('Time (days)')
ax2.set_ylabel('Magnification')
ax2.grid(True)

# animation functions
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    line1.set_data(time[:frame], [u(time[i], u0, t0, tE) for i in range(frame)])  # Dynamic Y-position
    line2.set_data(time[:frame], mag[:frame])
    return line1, line2

# learned a new matplotlib function to create an animation!
ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, repeat=False, interval=10)

plt.legend()
plt.show()
