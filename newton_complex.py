import matplotlib.pyplot as plt
import numpy as np

# Find roots of unity using Newton's method.

# Solve equation z^4 = 1 for complex z.
# Same as F(z) = z^4 - 1 = 0.

def F(z):
    return z**4 - 1

def Fp(z):
    return 4 * z**3


xmin, xmax = -2, 2
ymin, ymax = -2, 2
N = 500
kmax = 20

roots = np.zeros([N, N])

i = 0
j = 0

for x in np.linspace(xmin, xmax, N):
    for y in np.linspace(ymin, ymax, N):
        z = x + 1j * y
        k = 0
        tol = 1e-12

        # Newton's method
        while True:
            k += 1
            z_new = z - F(z) / Fp(z)
            
            if abs(z_new - z) < tol or k >= kmax:
                break

            z = z_new
        
        if abs(z_new - 1) < tol:
            roots[i, j] = 1
        elif abs(z_new + 1) < tol:
            roots[i, j] = 2
        elif abs(z_new - 1j) < tol:
            roots[i, j] = 3
        elif abs(z_new + 1j) < tol:
            roots[i, j] = 4
            
        i += 1
        
    i = 0
    j += 1

# print(roots)

fig, ax = plt.subplots()
c = ax.pcolor(roots)
fig.colorbar(c, ax=ax)
plt.show()