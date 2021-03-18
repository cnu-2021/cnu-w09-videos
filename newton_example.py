import matplotlib.pyplot as plt
import numpy as np

def F(x):
    return x ** 3 - x ** 2 + 0.1

def Fp(x):
    return 3.0 * (x ** 2) - 2.0 * x

def Fa(x, x_0, y_0, m):
    return m * (x - x_0) + y_0

pause_time = 2

# Plot the function
xmin, xmax = -0.5, 1.5
x = np.linspace(xmin, xmax, 10001)
fig, ax = plt.subplots(figsize=(10, 6))
ax.axhline(0.0, color = "#888888")
ax.plot(x, F(x), color = "k", linestyle = "-")
ax.set(xlabel=r"$x$", ylabel=r"$F(x)$", xlim=(xmin, xmax), ylim=(-0.1, 0.2))
plt.ion()
plt.show()

# Initial guess
x_sa = 0.7

for k in range(10):
    lab_k = ax.text((xmax + xmin)/2, 0.18, f'Iteration k = {k}',
                    horizontalalignment='center')
    
    # Current guess
    marker_line = ax.axvline(x_sa, color = "r", linestyle = ":")
    current_guess = ax.plot([x_sa], [F(x_sa)],
                            marker = "x", markersize = 10,
                            color = "r", markeredgewidth = 2)
    plt.pause(pause_time)

    # New tangent
    x_0, y_0, m = x_sa, F(x_sa), Fp(x_sa)

    xa = np.array([xmin, xmax])
    tangent = ax.plot(xa, Fa(xa, x_0, y_0, m), color = "r", linestyle = "-")
    plt.pause(pause_time)

    # Next guess
    x_sa = (-y_0 / m) + x_0

    next_guess = ax.plot([x_sa], [0.0],
                         marker = "x", markersize = 10,
                         color = "r", markeredgewidth = 2)
    plt.pause(pause_time)
    
    tangent[0].remove()
    current_guess[0].remove()
    marker_line.remove()
    next_guess[0].remove()
    lab_k.remove()