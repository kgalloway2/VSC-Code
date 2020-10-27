import math
import vector_functions as v 
import matrix_functions as m 

# initial values
x = [[[0.7],[0.7]]]
S = []
a = []

# functions and gradients

def f(x):
    return (x[0][0] - 1) ** 2 + x[1][0] ** 2

def g(x):
    return (x[0][0] ** 2) + (x[1][0] ** 2) - 1

def gradzf(z):
    return [[2 * z[1][0]  - 2] ]
    
def gradyf(y):
    return [[2 * y[1][0]]]

def gradzpsi(z):
    return [[2 * z[0][0]]]

def gradypsi(y):
    return [[2 * y[1][0]]]

def gradfR(x):
    a = v.transpose(gradzf(x))
    b = v.vector_mult(gradyf(x), v.vector_mult(m.inverse(gradypsi(x)),gradzpsi(x)))
    return v.vector_add(a,v.scalar_mult(-1,b))

def s(x):
    temp = gradfR(x)
    return v.scalar_mult(-1, temp)

def alpha(x,s): # found by checking a bunch of them. a = 0.0284 was best for 5 iterations
    return 0.00011

# algorithm
iterations = 0
while True and iterations < 5000:
    S.append(s(x[-1]))
    a.append(alpha(x[-1],S[-1]))
    change_z = v.scalar_mult(a[-1],S[-1])
    z = v.vector_add([x[-1][0]], change_z)
    change_y = v.vector_mult(m.inverse(gradypsi(x[-1])),v.vector_mult(gradzpsi(x[-1]),change_z))
    y = v.vector_add([x[-1][1]], v.scalar_mult(-1,change_y))
    #print(iterations,x[-1],a[-1],S[-1],change_z,change_y, f(x[-1]), g(x[-1]))
    x.append([z[0],y[0]])
    #print('error', abs(f(x[-1]) - f(x[-2])))
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break

print(iterations, x[-1], f(x[-1]),g(x[-1]),abs(f(x[-1]) - f(x[-2])))
