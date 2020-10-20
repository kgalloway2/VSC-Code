import math
import vector_functions as v
import matrix_functions as m  
import guassian as g 

'''based on assignment 3, problem 2. minimize a 2D f with 2 inequality constraints'''
'''changed since homework submission. still not working correctly'''

# initial guesses and stuff
x = [[[2.56155],[-1.56155]]]
Hessians = [[[1,0],[0,1]]]
l = []
penalties = []

# functions and gradients
def f(x):
    return (x[0][0] ** 2) + x[1][0]

def gradxf(x):
    return [[2 * x[0][0]],[1]]

def g1(x):
    return (x[0][0] ** 2) + (x[1][0] ** 2) - 9

def gradxg1(x):
    return [[2 * x[0][0]],[2 * x[1][0]]]

def g2(x):
    return x[0][0] + x[1][0] - 1

def gradxg2(x):
    return [[1],[1]]

def a(x,dx1,dx2):
    return (-2 * x * dx1 - dx2) / (2 * x * dx1 ** 2)

def gradxL(x,l):
    return [[gradxf(x)[0][0] - l[0] * gradxg1(x)[0][0] - l[1] * gradxg2(x)[0][0]],
    [gradxf(x)[1][0] - l[0] * gradxg1(x)[1][0] - l[1] * gradxg2(x)[1][0]]]

def hessian(H, gamma, change_x):
    gammat = v.transpose(gamma)
    xt = v.transpose(change_x)
    xxt = m.matrix_mult(change_x, xt)
    term1 = H
    term2 = m.scalar_mult(1 / v.dot(gamma,change_x),m.matrix_mult(gamma, gammat))
    term3 = m.scalar_mult(1 / v.dot(m.matrix_mult(xt,H),change_x),m.matrix_mult(H,m.matrix_mult(xxt, H)))
    return m.matrix_add(term1, m.matrix_add(term2, m.scalar_mult(-1, term3)))

# algorithm
print(x[-1],f(x[-1]),g1(x[-1]),g2(x[-1]))
iterations = 0
penalties.append(f(x[-1]))
while True and iterations < 50:
    # initial solve of system
    temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
    matrix = [[Hessians[-1][0][0],temp1,-gradxg1(x[-1])[0][0],-gradxg2(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                [temp1,Hessians[-1][1][1],-gradxg1(x[-1])[1][0],-gradxg2(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                [-gradxg1(x[-1])[0][0],-gradxg1(x[-1])[1][0],0,0,g1(x[-1])],
                [-gradxg2(x[-1])[0][0],-gradxg2(x[-1])[1][0],0,0,g2(x[-1])]]
    temp2 = g.gelim(matrix)
    new_x1 = x[-1][0][0] + temp2[0]
    new_x2 = x[-1][1][0] + temp2[1]
    new_l1 = temp2[2] 
    new_l2 = temp2[3]
    # if lambdas break KKT conditions, set lambdas to zero and re-solve matrix
    if new_l1 > 0 or new_l2 > 0:
        if new_l1 > 0 and new_l2 > 0: # set both to 0 and re-solve
            temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
            matrix = [[Hessians[-1][0][0],temp1,-gradxf(x[-1])[0][0]],
                    [temp1,Hessians[-1][1][1],-gradxf(x[-1])[1][0]]]
            temp2 = g.gelim(matrix)
            new_x1 = x[-1][0][0] + temp2[0]
            new_x2 = x[-1][1][0] + temp2[1]
            new_l1 = 0 
            new_l2 = 0
        elif new_l1 > 0 and new_l2 <= 0 : # set lambda1 to 0 and re-solve
            temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
            matrix = [[Hessians[-1][0][0],temp1,-gradxg2(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                        [temp1,Hessians[-1][1][1],-gradxg2(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                        [-gradxg2(x[-1])[0][0],-gradxg2(x[-1])[1][0],0,g2(x[-1])]]
            temp2 = g.gelim(matrix)
            new_x1 = x[-1][0][0] + temp2[0]
            new_x2 = x[-1][1][0] + temp2[1]
            new_l1 = 0
            new_l2 = temp2[2]
        elif new_l1 <= 0 and new_l2 > 0 : # set lambda2 to 0 and re-solve
            temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
            matrix = [[Hessians[-1][0][0],temp1,-gradxg1(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                        [temp1,Hessians[-1][1][1],-gradxg1(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                        [-gradxg1(x[-1])[0][0],-gradxg1(x[-1])[1][0],0,g1(x[-1])]]
            temp2 = g.gelim(matrix)
            new_x1 = x[-1][0][0] + temp2[0]
            new_x2 = x[-1][1][0] + temp2[1]
            new_l1 = temp2[2]
            new_l2 = 0
    
    l.append([new_l1,new_l2])
    alpha = a(x[-1][0][0],temp2[0],temp2[1])
    while True: # loop until penalty is not greater than previous 
        new_x1 = x[-1][0][0] + alpha * temp2[0]
        new_x2 = x[-1][1][0] + alpha * temp2[1]
        penalty = f([[new_x1],[new_x2]])
        if g1([[new_x1],[new_x2]]) > 0:
            penalty += new_l1 * abs(g1([[new_x1],[new_x2]]))
        if g2([[new_x1],[new_x2]]) > 0:
            penalty += new_l2 * abs(g2([[new_x1],[new_x2]]))
        if penalty <= penalties[-1]:
            penalties.append(penalty)
            x.append([[new_x1],[new_x2]])
            break
        else:
            alpha *= 0.7 # change step length
    print(iterations,'x:', x[-1],'lambdas:',l[-1], 'f(x) =',f(x[-1]))
    print('g1=', g1(x[-1]),'g2=',g2(x[-1]))
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.000005:
        break
    # compute new Hessian and go again
    gamma = v.vector_add(gradxL(x[-1], l[-1]), v.scalar_mult(-1,gradxL(x[-2],l[-1])))
    change_x = v.vector_add(x[-1],v.scalar_mult(-1,x[-2]))
    Hessians.append(hessian(Hessians[-1],gamma,change_x))

print(x[-1],f(x[-1]), g1(x[-1]),g2(x[-1]))