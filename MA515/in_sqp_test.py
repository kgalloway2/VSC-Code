import math
import vector_functions as v
import matrix_functions as m  
import guassian as g 

'''this is the best I could do for hw3p2. brute forced to find the best initial alpha value at the bottom'''

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
    # solve the four cases based on KKT conditions and keep the best that satisifies conditions
    options = []
    temp1 = 0.5 * (Hessians[-1][0][1] + Hessians[-1][1][0])
    matrix = [[Hessians[-1][0][0],temp1,-gradxg1(x[-1])[0][0],-gradxg2(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                [temp1,Hessians[-1][1][1],-gradxg1(x[-1])[1][0],-gradxg2(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                [-gradxg1(x[-1])[0][0],-gradxg1(x[-1])[1][0],0,0,g1(x[-1])],
                [-gradxg2(x[-1])[0][0],-gradxg2(x[-1])[1][0],0,0,g2(x[-1])]]
    temp2 = g.gelim(matrix)
    onenew_x1 = temp2[0]
    onenew_x2 = temp2[1]
    onenew_l1 = temp2[2] 
    onenew_l2 = temp2[3]
    if g1([[x[-1][0][0] + onenew_x1],[x[-1][1][0] + onenew_x2]]) <= 0 and g2([[x[-1][0][0] + onenew_x1],[x[-1][1][0] + onenew_x2]]) <= 0:
        options.append([[onenew_x1],[onenew_x2],[onenew_l1],[onenew_l2]])
    
    matrix = [[Hessians[-1][0][0],temp1,-gradxf(x[-1])[0][0]],
            [temp1,Hessians[-1][1][1],-gradxf(x[-1])[1][0]]]
    temp2 = g.gelim(matrix)
    twonew_x1 = temp2[0]
    twonew_x2 = temp2[1]
    twonew_l1 = 0 
    twonew_l2 = 0
    if g1([[x[-1][0][0] + twonew_x1],[x[-1][1][0] + twonew_x2]]) <= 0 and g2([[x[-1][0][0] + twonew_x1],[x[-1][1][0] + twonew_x2]]) <= 0:
        options.append([[twonew_x1],[twonew_x2],[twonew_l1],[twonew_l2]])    
    
    matrix = [[Hessians[-1][0][0],temp1,-gradxg2(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                [temp1,Hessians[-1][1][1],-gradxg2(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                [-gradxg2(x[-1])[0][0],-gradxg2(x[-1])[1][0],0,g2(x[-1])]]
    temp2 = g.gelim(matrix)
    threenew_x1 = temp2[0]
    threenew_x2 = temp2[1]
    threenew_l1 = 0
    threenew_l2 = temp2[2]
    if g1([[x[-1][0][0] + threenew_x1],[x[-1][1][0] + threenew_x2]]) <= 0 and g2([[x[-1][0][0] + threenew_x1],[x[-1][1][0] + threenew_x2]]) <= 0:
        options.append([[threenew_x1],[threenew_x2],[threenew_l1],[threenew_l2]])

    matrix = [[Hessians[-1][0][0],temp1,-gradxg1(x[-1])[0][0],-gradxf(x[-1])[0][0]],
                [temp1,Hessians[-1][1][1],-gradxg1(x[-1])[1][0],-gradxf(x[-1])[1][0]],
                [-gradxg1(x[-1])[0][0],-gradxg1(x[-1])[1][0],0,g1(x[-1])]]
    temp2 = g.gelim(matrix)
    fournew_x1 = temp2[0]
    fournew_x2 = temp2[1]
    fournew_l1 = temp2[2]
    fournew_l2 = 0
    if g1([[x[-1][0][0] + fournew_x1],[x[-1][1][0] + fournew_x2]]) <= 0 and g2([[x[-1][0][0] + fournew_x1],[x[-1][1][0] + fournew_x2]]) <= 0:
        options.append([[fournew_x1],[fournew_x2],[fournew_l1],[fournew_l2]])

    current_min = float('inf')
    for i in options:
        if f([[x[-1][0][0] + i[0][0]],[x[-1][1][0] + i[1][0]]]) < current_min:
            current_choice = i

    new_l1 = current_choice[2][0]
    new_l2 = current_choice[3][0]
    l.append([new_l1,new_l2])
    alpha = 0.1821
    while True: # loop until penalty is not greater than previous 
        new_x1 = x[-1][0][0] + alpha * current_choice[0][0]
        new_x2 = x[-1][1][0] + alpha * current_choice[1][0]
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
            alpha *= 0.5 # change step length
    print(iterations,'x:', x[-1],'lambdas:',l[-1], 'f(x) =',f(x[-1]))
    print('g1=', g1(x[-1]),'g2=',g2(x[-1]))
    iterations += 1
    if abs(f(x[-1]) - f(x[-2])) < 0.00005:
        break
    # compute new Hessian and go again
    gamma = v.vector_add(gradxL(x[-1], l[-1]), v.scalar_mult(-1,gradxL(x[-2],l[-1])))
    change_x = v.vector_add(x[-1],v.scalar_mult(-1,x[-2]))
    Hessians.append(hessian(Hessians[-1],gamma,change_x))

print(x[-1],f(x[-1]), g1(x[-1]),g2(x[-1]))
#return f(x[-1]),g1(x[-1]),g2(x[-1])

'''mini = float('inf')
for i in range(0,10000):
    cur,g1,g2 = function(i / 10000)
    if cur < mini and g1 <= 0 and g2 <= 0:
        mini = cur
        best_i = i / 10000

print(mini,best_i)'''