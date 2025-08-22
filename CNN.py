u1 = [[0, 0, 0, 0, 0], 
     [0, 1, 1, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0]]
u2 = [[0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0],
     [1, 0, 1, 0, 0],
     [1, 1, 1, 0, 0]]
u3 = [[0, 0, 0, 0, 0], 
     [1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0]]
w = [[1, 1, 1],
     [1, 0, 0],
     [1, 0, 0]]
teta = 2.5
def f(x):
    if (x < 0):
        return 0
    else:
        return 1 
def convolution(w, u):
    x = [[0]*5 for _ in range(5)]
    for i in range(0, 5):
        for j in range(0, 5):
            x[i][j] = 0
            for iprim in range(0, 3):
                for jprim in range(0, 3):
                    if not (i + iprim >= 5 or j + jprim >= 5):
                        x[i][j] += w[iprim][jprim] * u[i+iprim][j+jprim]
            x[i][j] = f(x[i][j] - teta)
    return x



print("ZAD 1")
x1 = convolution(w, u1)
x2 = (convolution(w, u2))
x3 = (convolution(w, u3))

print("x1")
for i in range(0, 5):
    for j in range(0, 5):
        print(x1[i][j], " ",end = "")
    print('\n')
print("x2")
for i in range(0, 5):
    for j in range(0, 5):
        print(x2[i][j], " ",end = "")
    print('\n')
print("x3")
for i in range(0, 5):
    for j in range(0, 5):
        print(x3[i][j], " ",end = "")
    print('\n')

print("ZAD 2")

teta = 2.5/9
x = [[0, 0, 1, 0, 0], 
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0]]
def pooling(x):
    y = [[0]*5 for _ in range(5)]
    for i in range(0, 5):
        for j in range(0, 5):
            y[i][j] = 0
            for iprim in range(0, 3):
                for jprim in range(0, 3):
                    if not (i + iprim >= 5 or j + jprim >= 5):
                        y[i][j] += x[i+iprim][j+jprim]
            y[i][j] = f(1/9*y[i][j] - teta)
    return y

y = pooling(x)
print("y")
for i in range(0, 5):
    for j in range(0, 5):
        print(y[i][j], " ",end = "")
    print('\n')