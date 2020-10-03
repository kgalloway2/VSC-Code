import math
import vector_functions as v
import guassian as g
import matrix_functions as m

''' minimize f(x) subject to h(x) = 0. worked for example he did on pg. 50.'''

# initial guesses and stuff
x = [[-0.7,-0.7]]
l = [-0.01]
p = []
n = []

# functions and gradients

def f(x):
    return math.e ** (3 * x[0] + 4 * x[1])

def gradxf(x):
    return [f(x) * 3, f(x) * 4]

def h(x):
    return (x[0] ** 2) + (x[1] ** 2) - 1

def gradxh(x):
    return [2 * x[0], 2 * x[1]]

def gradxL(x):
    return [gradxf(x)[0] - l[-1] * gradxh(x)[0],gradxf(x)[1] - l[-1] * gradxh(x)[1]]

def gradxxf(x):
    return [[gradxf(x)[0] * 3, gradxf(x)[0] * 4],[gradxf(x)[1] * 3, gradxf(x)[1] * 4]]

def gradxxh(x):
    return [[2,0],[0,2]]

def gradxxL(x):
    return m.matrix_add(gradxxf(x), m.scalar_mult(-l[-1],gradxxh(x)))

# algorithm

while True:
    matrix = [[gradxxL(x[-1])[0][0],gradxxL(x[-1])[0][1],-gradxh(x[-1])[0],-gradxL(x[-1])[0]],
              [gradxxL(x[-1])[1][0],gradxxL(x[-1])[1][1],-gradxh(x[-1])[1],-gradxL(x[-1])[1]],
              [-gradxh(x[-1])[0],-gradxh(x[-1])[1],0,h(x[-1])]]
    #print(matrix[0])
    #print(matrix[1])
    #print(matrix[2])
    temp = g.gelim(matrix)
    #print(temp)
    p.append([temp[0],temp[1]])
    n.append(temp[2])
    print(x[-1],l[-1],p[-1],n[-1])
    x.append(v.vector_add(x[-1], p[-1]))
    l.append(l[-1] +n[-1])
    if abs(f(x[-1]) - f(x[-2])) < 10 ** -4:
        break

print(x[-1],f(x[-1]))