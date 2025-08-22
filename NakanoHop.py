import copy
import random as r
import numpy as np
import matplotlib.pyplot as plt
def show(vector, title="x(t)"):
    matrix = np.array(vector).reshape((1, len(vector)))

    # Zamień -1 → 1 (biały), 1 → 0 (czarny)
    display_matrix = (1 - matrix) / 2

    fig, ax = plt.subplots()
    ax.imshow(display_matrix, cmap='gray', vmin=0, vmax=1)

    # Szare tło
    fig.patch.set_facecolor('#888888')
    ax.set_facecolor('#888888')

    # Ukryj osie
    ax.set_xticks([])
    ax.set_yticks([])

    # Tytuł wykresu
    ax.set_title(title, color='white', fontsize=14)

    plt.show()
def f(x):
    if x < 0:
        return -1
    else:
        return 1
def dotproduct(X, Y):
    sum = 0
    for i in range(0, len(X)):
        sum += X[i]*Y[i]
    return sum    
def round(X, W):
    NewX = copy.deepcopy(X)
    for i in range(len(X)):
        NewX[i] = f(dotproduct(X,W[i]))
    return NewX
t = 0
q1 = np.array([-1, -1, 1, -1, 0])
k1 = np.array([[-1, -1, 1, 0, 0]])   
q2 = np.array([1, 1, 1, 1, 0])
k2 = np.array([[1, 1, 1, 0, 0]]) 
q3 = np.array([1, -1, -1, -1, 0])
k3 = np.array([[1, -1, -1, 0, 0]])
q4 = np.array([-1, 1, -1, 1, 0])
k4 = np.array([[-1, 1, -1, 0, 0]])
v1 = np.array([[-1], [-1], [1], [-1], [-1]])
v2 = np.array([[1], [1], [1], [1], [-1]])
v3 = np.array([[1], [-1], [-1], [-1], [1]])
v4 = np.array([[-1], [1], [-1], [1], [1]]) 

W = np.matmul(v1, k1) + np.matmul(v2, k2) + np.matmul(v3, k3) + np.matmul(v4, k4) 
def simulate(X_init, label=""):
    X = X_init.copy()
    prev_X = None
    t = 0
    while not np.array_equal(X, prev_X):
        show(X, f"{label} x(t) dla t = {t}")
        prev_X = X.copy()
        X = round(X, W)
        t += 1
simulate(q1, "X = q1")
simulate(q2, "X = q2")
simulate(q3, "X = q3")
simulate(q4, "X = q4")
simulate(np.random.choice([-1, 1], size=5), "X = random")
