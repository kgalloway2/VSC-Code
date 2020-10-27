import math
import vector_functions as v
import matrix_functions as m  
import guassian as g 

'''based on example from class and not working becuase of KKT conditions that he never explains'''

# initial guesses and stuff
x = [[[-1],[4]]]
Hessians = [[[1,0],[0,1]]]
s = [[2.4375]]
l = [[2]]
mu = 5
penalties = []

# functions and gradients
def f(x):
    return (x[0][0] ** 4) - 2 * x[1][0] * (x[0][0] ** 2) + (x[1][0] ** 2) + (x[0][0] ** 2) - 2 * x[0][0] + 5

def gradxf(x):
    return [[4 * (x[0][0] ** 3) - 4 * x[1][0] * x[0][0] + 2 * x[0][0]- 2],[ - 2 * (x[0][0] ** 2) + 2 * x[1][0]]]

def g1(x):
    return -1 * ((x[0][0] + 0.25) ** 2) + 0.75 * x[1][0]

def gradxg1(x):
    return [[-2 * (x[0][0] + 0.25)],[0.75]]

def a():
    return 1

def gradxL(x,l):
    return [[gradxf(x)[0][0] - l[0] * gradxg1(x)[0][0]],
    [gradxf(x)[1][0] - l[0] * gradxg1(x)[1][0]]]

def gradsL(s,l,mu):
    return s[0] * l[0] - mu

def gradlL(x,s):
    return -(g1(x) - s[0])

def hessian(H, gamma, change_x):
    gammat = v.transpose(gamma)
    xt = v.transpose(change_x)
    xxt = m.matrix_mult(change_x, xt)
    term1 = H
    term2 = m.scalar_mult(1 / v.dot(gamma,change_x),m.matrix_mult(gamma, gammat))
    term3 = m.scalar_mult(1 / v.dot(m.matrix_mult(xt,H),change_x),m.matrix_mult(H,m.matrix_mult(xxt, H)))
    return m.matrix_add(term1, m.matrix_add(term2, m.scalar_mult(-1, term3)))

# algorithm
iterations = 0
penalties.append(f(x[-1]))
while True and iterations < 10:
    # initial solve of system
    temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
    matrix = [[Hessians[-1][0][0],temp1,0,-gradxg1(x[-1])[0][0],-gradxL(x[-1],l[-1])[0][0]],
                [temp1,Hessians[-1][1][1],0,-gradxg1(x[-1])[1][0],-gradxL(x[-1],l[-1])[1][0]],
                [0,0,l[-1][0],s[-1][0],-gradsL(s[-1],l[-1],mu)],
                [gradxg1(x[-1])[0][0],gradxg1(x[-1])[1][0],-1,0,-gradlL(x[-1],s[-1])]]
    temp2 = g.gelim(matrix)
    
    alpha = a()
    while s[-1][0] + alpha * temp2[2] < 0:
        alpha *= 0.748
    new_s = s[-1][0] + alpha * temp2[2]
    s.append([new_s])
    
    alpha = a()
    while new_s * (l[-1][0] + alpha * temp2[3]) - mu < 0:
        alpha *= 0.5
    new_l = l[-1][0] + alpha * temp2[3]
    l.append([new_l])

    alpha = a()
    while True: # loop until penalty is not greater than previous 
        new_x1 = x[-1][0][0] + alpha * temp2[0]
        new_x2 = x[-1][1][0] + alpha * temp2[1]
        penalty = f([[new_x1],[new_x2]])
        if g1([[new_x1],[new_x2]]) < 0:
            penalty += 5 * abs(g1([[new_x1],[new_x2]]))
        if penalty <= penalties[-1]:
            penalties.append(penalty)
            x.append([[new_x1],[new_x2]])
            break
        else:
            alpha *= 0.27 # change step length
    print(iterations,'x:', x[-1],'lambdas:',l[-1], 's',s[-1],'f(x) =',f(x[-1]))
    print('g1=', g1(x[-1]),'-----------------')
    mu /= 5
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.000005:
        break
    # compute new Hessian and go again
    gamma = v.vector_add(gradxL(x[-1], l[-1]), v.scalar_mult(-1,gradxL(x[-2],l[-1])))
    change_x = v.vector_add(x[-1],v.scalar_mult(-1,x[-2]))
    Hessians.append(hessian(Hessians[-1],gamma,change_x))

print(x[-1],f(x[-1]), g1(x[-1]))