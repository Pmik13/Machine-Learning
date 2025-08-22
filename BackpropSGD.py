import numpy as np
import random as r
import copy
beta = 2.0
eps = 0.0001
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
        return 1
    if p == 2:
        return 1
    if p == 3:
        return 0
def check(s, s2):
    ret = 0
    for i in range(len(s)):
        ret = max(ret, abs(s[i] - s2[i]))
    return ret
def ANS(U, W, S):
    x = X(U, W)
    ans = f(dotproduct(x, S))
    return ans
def X(U, W):
    x = [0, 0, 1]
    for i in range(0, 2):
        x[i] = f(dotproduct(W[i], U))
    return x
def error(U, W, S, Y):
    ans= ANS(U, W, S)
    return pow(ans - Y, 2)
N = 1
w1 = r.randint(-N, N)
w2 = r.randint(-N, N)
w3 = r.randint(-N, N)
w4 = r.randint(-N, N)
w5 = r.randint(-N, N)
w6= r.randint(-N, N)
s1 = r.randint(-N, N)
s2 = r.randint(-N, N)
s3 = r.randint(-N, N)

Wnew = [[w1, w2, w3],[w3, w4, w5]]
Snew = [s1, s2, s3]

p = r.randint(0, 3)

U = u(p)
Y = y(p)

print("W:", Wnew)
print("U:", U)

sold = -100000

W = [[-200, -200, -200], [-200, -200, -200]]
S = [-200, -200, -200]
count = 0 
while(max(check(Snew, S), max(check(Wnew[0], W[0]), check(Wnew[1], W[1])))> eps):
    count+=1

    W = copy.deepcopy(Wnew)
    S = Snew[:]
    changeW = [[0, 0, 0], [0, 0, 0]]
    changeS = [0, 0, 0]
    p = r.randint(0, 3)
    U = u(p)
    Y = y(p)
    x = X(U,W)
    changeS[0] +=  c*(ANS(U, W, S) - Y) * (derivative_f((dotproduct(S, x ))))*x[0]
    
    changeS[1] += c*(ANS(U, W, S) - Y) * (derivative_f((dotproduct(S, x))))*x[1]

    changeS[2] +=  c*(ANS(U, W, S) - Y) * (derivative_f((dotproduct(S, x))))*x[2]
    
    
    #print("wagiS: ", Snew, "   iteracje: ", count, "error: ")

    U = u(p)
    Y = y(p)
    x = X(U,W)
    for i in range(0, 2):
        changeW[i][0] +=  c*(ANS(U, W, S) - Y) * (derivative_f((dotproduct(S, x)))) * S[i] * (derivative_f((dotproduct(W[i], U)))) * U[0]
    
        changeW[i][1] += c*(ANS(U, W, S) - Y) * (derivative_f((dotproduct(S, x)))) * S[i] * (derivative_f((dotproduct(W[i], U)))) * U[1]

        changeW[i][2] +=  c*(ANS(U, W, S) - Y) * (derivative_f((dotproduct(S, x)))) * S[i] * (derivative_f((dotproduct(W[i], U)))) * U[2]

    Snew[0] = S[0] - changeS[0]
    Snew[1] = S[1] - changeS[1]
    Snew[2] = S[2] - changeS[2]

    for i in range(0, 2):
        for j in range(0, 3):
            Wnew[i][j] = W[i][j] - changeW[i][j]


print("wagi: ", Wnew, "   iteracje: ", count, "error: ")
er = 0
for i in range(0, 4):
    U = u(i)
    Y = y(i)
    print("y(" + str(i) + ") : " + str( ANS(U, Wnew, Snew)))
    er += error(U, Wnew, Snew, Y)
print("eror : ", 1/2*er)
