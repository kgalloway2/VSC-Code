import math
import vector_functions as v 
import matrix_functions as m 

'''2d f with single constraint g. based on hw3p1b. not very accurate because of inexact line search''' 

# initial values
x = [[[0.5],[1.5]]]
S = []
a = []

# functions and gradients

def f(x):
    return (x[0][0] ** 2) + (x[1][0] ** 2)

def g(x):
    return x[0][0] + x[1][0] - 2

def gradzf(z):
    return [2 * z[0][0]] 
    
def gradyf(y):
    return [2 * y[1][0]]

def gradzpsi(z):
    return [1]

def gradypsi(y):
    return [1]

def gradfR(x):
    a = [gradzf(x)]
    b = [gradyf(x)]
    return v.vector_add(a,v.scalar_mult(-1,b))

def s(x):
    temp = gradfR(x)
    #c = v.euc_norm(temp) # don't use the norm becuase s is a singleton so normalizing would just use 1 every time
    return v.scalar_mult(-1, temp)

def alpha(x,s): # just going to guess it
    return 0.2

# algorithm
iterations = 0
while True:
    S.append(s(x[-1]))
    a.append(alpha(x[-1],S[-1]))
    change_z = v.scalar_mult(a[-1],S[-1])
    z = v.vector_add([x[-1][0]], change_z)
    change_y = v.vector_mult([[1]],v.vector_mult([[1]],change_z))
    y = v.vector_add([x[-1][1]], v.scalar_mult(-1,change_y))
    print(iterations,x[-1],a[-1],S[-1],change_z,change_y, f(x[-1]))
    x.append([z[0],y[0]])
    print('error', abs(f(x[-1]) - f(x[-2])))
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break

print(iterations, x[-1], f(x[-1]),abs(f(x[-1]) - f(x[-2])))