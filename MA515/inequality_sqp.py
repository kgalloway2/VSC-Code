import math
import vector_functions as v
import matrix_functions as m  
import guassian as g 

'''based on assignment 3, problem 2. minimize a 2D f with 2 inequality constraints'''
'''not currently working. current theory is lambda = 0 vs g = 0 in checking kkt conditions is not correct'''

# initial guesses and stuff
x = [[[2.56155],[-1.56155]]]
Hessians = [[[1,0],[0,1]]]
l = []

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
iterations = 0
while True and iterations < 5:
    # initial solve of system
    temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
    matrix = [[Hessians[-1][0][0],temp1,-gradxg1(x[-1])[0][0],-gradxg2(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                [temp1,Hessians[-1][1][1],-gradxg1(x[-1])[1][0],-gradxg2(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                [-gradxg1(x[-1])[0][0],-gradxg1(x[-1])[1][0],0,0,g1(x[-1])],
                [-gradxg2(x[-1])[0][0],-gradxg2(x[-1])[1][0],0,0,g2(x[-1])]]
    temp2 = g.gelim(matrix)
    #print(temp2)
    
    new_l1 = temp2[2] 
    new_l2 = temp2[3]
    # if new lambdas break KKT conditions, set them to zero and re-solve matrix
    if new_l1 > 0 or new_l2 > 0:
        if new_l1 > 0 and new_l2 > 0: # set both to 0 and re-solve
            temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
            matrix = [[Hessians[-1][0][0],temp1,-gradxf(x[-1])[0][0]],
                    [temp1,Hessians[-1][1][1],-gradxf(x[-1])[1][0]]]
            temp2 = g.gelim(matrix)
            new_l1 = 0 
            new_l2 = 0
        elif new_l1 > 0 and new_l2 <= 0 : # set lambda1 to 0 and re-solve
            temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
            matrix = [[Hessians[-1][0][0],temp1,-gradxg2(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                        [temp1,Hessians[-1][1][1],-gradxg2(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                        [-gradxg2(x[-1])[0][0],-gradxg2(x[-1])[1][0],0,g2(x[-1])]]
            temp2 = g.gelim(matrix)
            new_l1 = 0
            new_l2 = temp2[2]
        elif new_l1 <= 0 and new_l2 > 0 : # set lambda2 to 0 and re-solve
            temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
            matrix = [[Hessians[-1][0][0],temp1,-gradxg1(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                        [temp1,Hessians[-1][1][1],-gradxg1(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                        [-gradxg1(x[-1])[0][0],-gradxg1(x[-1])[1][0],0,g1(x[-1])]]
            temp2 = g.gelim(matrix)
            new_l1 = temp2[2]
            new_l2 = 0
    

    l.append([new_l1,new_l2])
    alpha = 1
    while True: # loop until penalty is less than previous 
        new_x1 = x[-1][0][0] + alpha * temp2[0]
        new_x2 = x[-1][1][0] + alpha * temp2[1]
        penalty = f([[new_x1],[new_x2]])
        if g1([[new_x1],[new_x2]]) > 0:
            penalty += new_l1 * abs(g1([[new_x1],[new_x2]]))
        if g2([[new_x1],[new_x2]]) > 0:
            penalty += new_l2 * abs(g2([[new_x1],[new_x2]]))
        if penalty < f(x[-1]):
            x.append([[new_x1],[new_x2]])
            break
        else:
            alpha *= 0.5 # change step length. just guessing instead of line search
    print(iterations,'x:', x[-1],'lambdas:',l[-1], 'f(x)=',f(x[-1]))
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break
    
    # compute new Hessian and go again
    gamma = v.vector_add(gradxL(x[-1], l[-1]), v.scalar_mult(-1,gradxL(x[-2],l[-1])))
    change_x = v.vector_add(x[-1],v.scalar_mult(-1,x[-2]))
    Hessians.append(hessian(Hessians[-1],gamma,change_x))
    print('-----------------------------------------------------------------------------')


print(x[-1],f(x[-1]))