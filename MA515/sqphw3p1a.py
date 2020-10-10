import math
import vector_functions as v
import guassian as g
import matrix_functions as m

''' minimize f(x) subject to h(x) = 0. hw 3 problem 1a.'''

# initial guesses and stuff
x = [[[0],[2 ** 0.5]]]
l = [-0.01]
p = []
n = []

# functions and gradients

def f(x):
    return (100 * ((x[1][0] - x[0][0]) ** 2)) + ((1 - x[0][0]) ** 2)

def gradxf(x):
    return [-200 * x[1][0] + 202 * x[0][0] -2, 200 * x[1][0] - 200 *x[0][0]]

def h(x):
    return (x[0][0] ** 2) + (x[1][0] ** 2) - 2

def gradxh(x):
    return [2 * x[0][0], 2 * x[1][0]]

def gradxL(x):
    return [gradxf(x)[0] - l[-1] * gradxh(x)[0],gradxf(x)[1] - l[-1] * gradxh(x)[1]]

def gradxxf(x):
    return [[202, -200],[-200, 200]]

def gradxxh(x):
    return [[2,0],[0,2]]

def gradxxL(x):
    return m.matrix_add(gradxxf(x), m.scalar_mult(-l[-1],gradxxh(x)))

# algorithm
iteration = 0
while True:
    
    matrix = [[gradxxL(x[-1])[0][0],gradxxL(x[-1])[0][1],-gradxh(x[-1])[0],-gradxL(x[-1])[0]],
              [gradxxL(x[-1])[1][0],gradxxL(x[-1])[1][1],-gradxh(x[-1])[1],-gradxL(x[-1])[1]],
              [-gradxh(x[-1])[0],-gradxh(x[-1])[1],0,h(x[-1])]]
    #print(matrix[0])
    #print(matrix[1])
    #print(matrix[2])
    temp = g.gelim(matrix)
    #print(temp)
    p.append([[temp[0]],[temp[1]]])
    n.append(temp[2])
    print(iteration,x[-1],l[-1],p[-1],n[-1], f(x[-1]))
    x.append(v.vector_add(x[-1], p[-1]))
    l.append(l[-1] +n[-1])
    print('error', abs(f(x[-1]) - f(x[-2])))
    iteration += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break

print(iteration, x[-1],f(x[-1]), abs(f(x[-1]) - f(x[-2])))