import math
import vector_functions as v 
import matrix_functions as m 

'''based on his example from pg. 58'''
'''currently not working.'''

# initial values
x = [[[2],[2],[2]]]
S = []
a = []

# functions and gradients

def f(x):
    return 4 * (x[0][0] ** 2) + (x[1][0] ** 2) + 3 * (x[2][0] ** 2)

def g(x):
    return 2 * x[0][0] + 4 * x[1][0] - x[2][0]

def gradzf(z):
    return [[2 * z[1][0]] ,[6 * z[2][0]]]
    
def gradyf(y):
    return [[8 * y[0][0]]]

def gradzpsi(z):
    return [[4, -1]]

def gradypsi(y):
    return [[2]]

def gradfR(x):
    a = v.transpose(gradzf(x))
    b = v.vector_mult(gradyf(x), v.vector_mult(m.inverse(gradypsi(x)),gradzpsi(x)))
    return v.vector_add(a,v.scalar_mult(-1,b))

def s(x):
    temp = v.transpose(gradfR(x))
    c = v.euc_norm(temp)
    return v.scalar_mult(-1/c, temp)

def alpha(x,s): # just going to guess it
    return 0.0001

# algorithm
iterations = 0
while True and iterations < 100000:
    S.append(s(x[-1]))
    a.append(alpha(x[-1],S[-1]))
    change_z = v.scalar_mult(a[-1],S[-1])
    z = v.vector_add(x[-1][0:2], change_z)
    change_y = v.vector_mult(m.inverse(gradypsi(x[-1])),[v.vector_mult(gradzpsi(x[-1]),change_z)])
    y = v.vector_add([x[-1][1]], v.scalar_mult(-1,change_y))
    #print(iterations,x[-1],a[-1],S[-1],change_z,change_y, f(x[-1]),g(x[-1]))
    x.append([y[0],z[0],z[1]])
    #print('error', abs(f(x[-1]) - f(x[-2])))
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break

print(iterations, x[-1], f(x[-1]),g(x[-1]),abs(f(x[-1]) - f(x[-2])))