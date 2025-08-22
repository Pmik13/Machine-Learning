import numpy as np
import random as r
beta = 2.0
eps = 0.001
c = 0.1
def f(x):
    ans = 1 / (1 + np.exp(-beta*x))
    return ans

def derivative_f(x):
    fx = f(x)
    return beta * fx * (1 - fx)
def dotproduct(X, Y):
    sum = 0
    for i in range(0, len(X)):
        sum += X[i]*Y[i]
    return sum
def u(p):
    if p == 0:
        return [0, 0, 1]
    if p == 1:
        return [0, 1, 1]
    if p == 2:
        return [1, 0, 1]
    if p == 3:
        return [1, 1, 1]
def y(p):
    if p == 0:
        return 0
    if p == 1:
        return 0
    if p == 2:
        return 0
    if p == 3:
        return 1
def error(W):
    sum = 0
    for p in range(0, 4):
        U = u(p)
        Y = y(p)
        s = f(dotproduct(W, U))
        sum += pow(s-Y, 2)
    return 1/2*sum
def check(s, s2):
    ret = 0
    for i in range(len(s)):
        ret = max(ret, abs(s[i] - s2[i]))
    return ret


N = 1
w1 = r.randint(0, N)
w2 = r.randint(0, N)
w3 = r.randint(0, N)

Wnew = [w1, w2, w3]

p = r.randint(0, 3)

U = u(p)
Y = y(p)

print("W:", Wnew)
print("U:", U)

sold = -100000
snew = error(Wnew)
W = [-200, -200, -200]
i = 0 
while(check(Wnew, W) > eps):
    i+=1
    sold = snew
    W = Wnew.copy()
    change = [0, 0, 0]
    for p in range(0, 4):
        U = u(p)
        Y = y(p)
        change[0] +=  c*(f(dotproduct(W, U)) - Y) * (derivative_f((dotproduct(W, U))))*U[0]
        
        change[1] += c*(f(dotproduct(W, U)) - Y) * (derivative_f((dotproduct(W, U))))*U[1]

        change[2] +=  c*(f(dotproduct(W, U)) - Y) * (derivative_f((dotproduct(W, U))))*U[2]
    print(error(Wnew))
    Wnew[0] = W[0] - change[0]
    Wnew[1] = W[1] - change[1]
    Wnew[2] = W[2] - change[2]
    print(error(Wnew))
    snew = error(W)
print("wagi: ", Wnew, "   iteracje: ", i, "error: ", error(Wnew))
for i in range (0, 4):
    U = u(p)
    Y = y(p)
    print(f(dotproduct(Wnew, U)) - Y)




