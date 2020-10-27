import math
import vector_functions as v
import matrix_functions as m  
import guassian as g 

# initial guesses and stuff
x = [[[1.1],[2]]]
Hessians = [[[1,0],[0,1]]]
s = [[[x[-1][0][0] - 1],[x[-1][1][0] + 1]]]
mu = 6.5
l = [[[(mu / s[-1][0][0])],[(mu / s[-1][1][0])]]]
penalties = []

# functions and gradients
def f(x):
    return (x[0][0] ** 2) + (x[1][0] ** 2) - mu * (math.log(s[-1][0][0]) + math.log(s[-1][1][0]))

def gradxf(x):
    return [[2 * x[0][0]],[2 * x[1][0]]]

def g1(x):
    return x[0][0] - 1 - s[-1][0][0]

def gradxg1(x):
    return [[1],[0]]

def g2(x):
    return x[1][0] + 1 - s[-1][1][0]

def gradxg2(x):
    return [[0], [1]]

def a():
    return 0.518

def gradxL(x,l):
    return [[gradxf(x)[0][0] - l[0][0]],
            [gradxf(x)[1][0] - l[1][0]]]

def gradsL(s,l,mu):
    return [[s[0][0] * l[0][0] - mu],
            [s[1][0] * l[1][0] - mu]]

def gradlL(x,s):
    return [[-(x[0][0] - 1 - s[0][0])],
            [-(x[1][0] + 1 - s[1][0])]]

def hessian(H, gamma, change_x):
    gammat = v.transpose(gamma)
    xt = v.transpose(change_x)
    xxt = m.matrix_mult(change_x, xt)
    term1 = H
    term2 = m.scalar_mult(1 / v.dot(gamma,change_x),m.matrix_mult(gamma, gammat))
    term3 = m.scalar_mult(1 / v.dot(m.matrix_mult(xt,H),change_x),m.matrix_mult(H,m.matrix_mult(xxt, H)))
    return m.matrix_add(term1, m.matrix_add(term2, m.scalar_mult(-1, term3)))

print('x:', x[-1],'lambdas:',l[-1],'s:',s[-1])
print('f(x) =',f(x[-1]))
print('g1=', g1(x[-1]),'g2=', g2(x[-1]),'-----------------')

# algorithm
iterations = 0
penalties.append(f(x[-1]))
while True and iterations < 50:
    mu /= 6.5
    # initial solve of system
    temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
    matrix = [[Hessians[-1][0][0],temp1,0,0,1,0,-2 * x[-1][0][0]],
                [temp1,Hessians[-1][1][1],0,0,0,1,-2 * x[-1][1][0]],
                [0,0,l[-1][0][0],0,s[-1][0][0],0,-gradsL(s[-1],l[-1],mu)[0][0]],
                [0,0,0,l[-1][1][0],0,s[-1][1][0],-gradsL(s[-1],l[-1],mu)[1][0]],
                [1,0,-1,0,0,0,-gradlL(x[-1],s[-1])[0][0]],
                [0,1,0,-1,0,0,-gradlL(x[-1],s[-1])[1][0]]]
    temp2 = g.gelim(matrix)
    
    alpha = a()
    while s[-1][0][0] + alpha * temp2[4] < 0 or s[-1][1][0] + alpha * temp2[5] < 0:
        alpha *= 0.5
    new_s1 = s[-1][0][0] + alpha * temp2[4]
    new_s2 = s[-1][1][0] + alpha * temp2[5]
    s.append([[new_s1],[new_s2]])
    alpha_s = alpha

    alpha = a()
    new_l1 = l[-1][0][0] + alpha * temp2[2]
    new_l2 = l[-1][1][0] + alpha * temp2[3]
    l.append([[new_l1],[new_l2]])
    
    while True: # loop until penalty is not greater than previous 
        new_x1 = x[-1][0][0] + alpha * temp2[0]
        new_x2 = x[-1][1][0] + alpha * temp2[1]
        penalty = f([[new_x1],[new_x2]])
        if g1([[new_x1],[new_x2]]) < 0:
            penalty += mu * abs(g1([[new_x1],[new_x2]]))
        if g2([[new_x1],[new_x2]]) < 0:
            penalty += mu * abs(g2([[new_x1],[new_x2]]))
        if penalty <= penalties[-1]:
            penalties.append(penalty)
            x.append([[new_x1],[new_x2]])
            break
        else:
            alpha *= 0.5 # change step length
    print(iterations,'x:', x[-1],'lambdas:',l[-1], 'a:',alpha,'s:',s[-1],'a_s:',alpha_s)
    print('f(x) =',f(x[-1]), 'error:',abs(f(x[-1]) - f(x[-2])))
    print('g1=', g1(x[-1]),'g2=', g2(x[-1]),'-----------------')
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break
    # compute new Hessian and go again
    gamma = v.vector_add(gradxL(x[-1], l[-1]), v.scalar_mult(-1,gradxL(x[-2],l[-1])))
    change_x = v.vector_add(x[-1],v.scalar_mult(-1,x[-2]))
    Hessians.append(hessian(Hessians[-1],gamma,change_x))

print(x[-1],f(x[-1]), g1(x[-1]), g2(x[-1]))