import random as r
import numpy as np
import matplotlib.pyplot as plt


beta = 2.5
def dotproduct(X, Y):
    sum = 0
    for i in range(0, len(X)):
        sum += X[i]*Y[i]
    return sum
def f(x):
    z = beta * x
    z = np.clip(z, -100, 100)
    return 1 / (1 + np.exp(-z))
import matplotlib.pyplot as plt
import numpy as np

def show(vector, title="Obraz 3x3"):
    
    matrix = np.array(vector).reshape((len(vector) // 3, 3))

    fig, ax = plt.subplots()
    ax.imshow(1 - matrix, cmap='gray', vmin=0, vmax=1)

    # Szare tło
    fig.patch.set_facecolor('#888888')
    ax.set_facecolor('#888888')

    # Ukryj osie
    ax.set_xticks([])
    ax.set_yticks([])

    # Tytuł wykresu
    ax.set_title(title, color='white', fontsize=14)

    plt.show()

def derivative_f(x):
    fx = f(x)
    return beta * fx * (1 - fx)
def uf(p):
    if p == 0:
        return [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]
    if p == 1:
        return [0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
def yf(p):
    if p == 1:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if p == 2:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
def w(p):
    if p == 1:
        return [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]
    if p == 2:
        return [0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
def xf(w, u):
    r1 = r.randint(-N, N)
    r2 = r.randint(-N, N)
    x = [r1, r2, 1]
    for i in range(0, 2):
        x[i] = f(dotproduct(w[i], u))
    return x
def yf(x, s):
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 9):
        y[i] = f(s[0][i]*x[0] + s[1][i]*x[1] + s[2][i]*x[2])
    return y
#print("ZAD 1")
N = r.randint(1, 10)
p = r.randint(0,1)
w = []
w.append([20, 0, 0, 0, 0, 0, 0, 0, 0, -10])
w.append([0, 0, 20, 0, 0, 0, 0, 0, 0, -10])
x = xf(w, u = uf(p))
s = [[20, 20, 0, 0, 20, 0, 0, 20, 0, 20],[0, 0, 20, 0, 0, 20, 0, 0, 20, 20],[-10, -10, -10, -10, -10, -10, -10, -10, -10, -10]]
show(x, "Zad 1 x(p) dla p = " + str(p))
show(yf(x, s), "Zad 1 y(p)")
#print("ZAD 2")
def train(s, w):
    for p in range(0,2):
        u = uf(p)
        x = xf(w, u)
        y = yf(x, s)
        sum = 0
        for j in range(0,9):
            for i in range(0, 3):
                for k in range(0, 3):
                    sum += s[k][j] * x[k]
                s[i][j] += (y[j] - u[j]) * derivative_f(sum) * x[i]

    for p in range(0,2):
        u = uf(p)
        x = xf(w, u)
        y = yf(x, s)
        sum = 0
        sum2 = 0
        for t in range(0,9):
            for j in range(0,10):
                for i in range(0, 2):
                    for k in range(0, 3):
                        for l in range(0, 10):
                            sum2 += w[i][l] * u[l]
                        sum += s[k][t] * x[k]                    
                    w[i][j] += (y[t] - u[t]) * derivative_f(sum)* s[i][t]* derivative_f(sum2) * u[j]

train(s, w)
for p in range(0, 2):
    u = uf(p)
    x = xf(w, u)
    show(x, "Zad 2 x(p) dla p = " + str(p))
    show(yf(x, s), "Zad 2 y(p) dla p = " + str(p))
#print("ZAD 3")
w = []
for j in range(0, 2):
    k = []
    for i in range(0, 10):
        k.append(r.uniform(-N, N))
    w.append(k)
s = []
for j in range(0, 3):
    k = []
    for i in range(0, 10):
        k.append(r.uniform(-N, N))
    s.append(k)
train(s, w)
for p in range(0, 2):
    u = uf(p)
    x = xf(w, u)
    show(x, "Zad 3 x(p) dla p = " + str(p))
    show(yf(x, s), "ZAD 3 y(p) dla p = " + str(p))
