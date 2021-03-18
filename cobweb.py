import matplotlib.pyplot as plt
import numpy as np

# Solve x - cos(x) - 1 = 0.

# Display text labels on plot
show_labels = False
pause_time = 2

# Iteration function
# def G(x):
#     return np.cos(x) + 1

# def G(x):
#     return np.arccos(x - 1)

# # Newton's method
# def G(x):
#     def F(x):
#         return x - np.cos(x) - 1
    
#     def Fp(x):
#         return 1 + np.sin(x)
    
#     return x - F(x) / Fp(x)

# Newton's method
def G(x):
    def F(x):
        return x ** 3 - x ** 2 + 0.1

    def Fp(x):
        return 3.0 * (x ** 2) - 2.0 * x
    
    return x - F(x) / Fp(x)

# Set parameters
x0 = 0.65
k = 0
tol = 1e-8

# Plot y=x and y=G(x)
fig, ax = plt.subplots(figsize=(10, 6))

xmin, xmax = -2, 2
x = np.linspace(xmin, xmax, 500)
ax.plot(x, x, 'b-', label=r'$y = x$')
ax.plot(x, G(x), 'r-', label=r'$y = \cos x + 1$')
# ax.set(xlim=[xmin, xmax], ylim=[xmin, xmax])
ax.set(xlim=[xmin, xmax], ylim=[-10, 5])
# ax.legend()

text_box = {'facecolor': [1, 1, 1], 'alpha': 0.8}
pos = 1.05

plt.ion()
plt.show()
plt.pause(1)

while True:
    
    lab_k = ax.text((xmax + xmin)/2, 0.95*xmax, f'Iteration k = {k}',
                    horizontalalignment='center')
    
    if show_labels:
        ax.plot(x0, x0, 'g', marker='.')
        lab0 = ax.text(x0, pos*x0, f'x{k}',
                    bbox=text_box,
                    horizontalalignment='center')
        plt.pause(pause_time)
    
    # Fixed point iteration
    x_new = G(x0)
    
    ax.plot([x0, x0], [x0, x_new], 'g', marker='.')
    if show_labels:
        lab1 = ax.text(x0, pos*x_new, f'G(x{k})',
                    bbox=text_box,
                    horizontalalignment='center')
    plt.pause(pause_time)
    
    ax.plot([x0, x_new], [x_new, x_new], 'g', marker='.')
    if show_labels:
        lab2 = ax.text(x_new, pos*x_new, f'x{k+1} = G(x{k})',
                    bbox=text_box,
                    horizontalalignment='center')
    plt.pause(pause_time)
    
    lab_k.remove()
    if show_labels:
        lab0.remove()
        lab1.remove()
        lab2.remove()

    if abs(x_new - x0) <= tol:
        break
    
    k += 1
    x0 = x_new

print(f'Root = {x_new}, found in {k} iterations')