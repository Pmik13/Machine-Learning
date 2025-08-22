import random as r
import numpy as np
n = 25

# Inicjalizacja x jako lista stanów (czas), każdy stan to lista 25 bitów
x = [ [r.randint(0, 1) for _ in range(n)] ]
T = -2
# Wzorce
z = [ 0, 0, 0 , 0 , 0,
      0, 1, 1 , 0 , 0,
      0, 0, 1 , 0 , 0,
      0, 0, 1 , 0 , 0,
      0, 0, 1 , 0 , 0 ]

zprim = [ 0, 1, 1 , 1 , 0,
          0, 1, 0 , 1 , 0,
          0, 1, 0 , 1 , 0,
          0, 1, 0 , 1 , 0,
          0, 1, 1 , 1 , 0 ]

# Funkcja korelacji
def c(z, i, j):
    if i == j:
        return 0
    return (2 * z[i] - 1) * (2 * z[j] - 1)

# Inicjalizacja wag i progów
w = [[0 for _ in range(n)] for _ in range(n)]
teta = [0 for _ in range(n)]

# Uczenie sieci (dla z i zprim)
for i in range(n):
    for j in range(n):
        w[i][j] = 8 * (c(z, i, j))

for i in range(n):
    for j in range(n):
        teta[i] += 4 * (c(z, i, j))

# Funkcja aktywacji
def f(u_i):
    beta = r.uniform(0, 1)
    f = 1 / (1 + np.exp(-u_i / T))
    return 1 if beta < f else 0

# Oblicz u[i] w czasie t
def ut(w, x_t, teta):
    u = [0] * n
    for i in range(n):
        for j in range(n):
            u[i] += w[i][j] * x_t[j]
        u[i] -= teta[i]
    return u

# Oblicz x[t] na podstawie x[t-1]
def xt(w, x, t):
    u = ut(w, x[t - 1], teta)
    new_x = [f(u[i]) for i in range(n)]
    return new_x

print("ZAD 1")
# Symulacja
for t in range(1, 10):
    x.append(xt(w, x, t))
    print(f"Iteration {t}:")
    for i in range(n):
        print(x[t][i], end=" ")
        if (i + 1) % 5 == 0:
            print()
    print()

print("ZAD 2")
x = [ [r.randint(0, 1) for _ in range(n)] ]
w = [[0 for _ in range(n)] for _ in range(n)]
teta = [0 for _ in range(n)]
T = 30 #  - 1.8  -2.5
# Uczenie sieci (dla z i zprim)
for i in range(n):
    for j in range(n):
        w[i][j] = 8 * (c(z, i, j) + c(zprim, i, j))

for i in range(n):
    for j in range(n):
        teta[i] += 4 * (c(z, i, j) + c(zprim, i, j))

for t in range(1, 10):
    x.append(xt(w, x, t))
    print(f"Iteration {t}:")
    for i in range(n):
        print(x[t][i], end=" ")
        if (i + 1) % 5 == 0:
            print()
    print()

