import math
import vector_functions as v
import matrix_functions as m  

'''unfinished and not even close.'''

H2 = [[17.7529,5.3882],[5.3882,1.9137]]
gamma2 = [[2.898],[-1.124]]
change_x2 = [[1.004],[-2.566]]

H1 = [[1,0],[0,1]]
gamma1 = [[-21],[-7]]
change_x1 = [[-0.5],[-2.25]]

H3 = [[13.3475,4.0939],[4.0939,2.0403]]
gamma3 = [[2.226],[1.848]]
change_x3 = [[0.1399],[0.8046]]

H4 = [[5.4633,1.8167],[1.8167,1.9809]]
gamma4 = [[2.519],[-0.1688]]
change_x4 = [[0.6099],[-0.1474]]

def hessian(H, gamma, change_x):
    gammat = v.transpose(gamma)
    xt = v.transpose(change_x)
    xxt = m.matrix_mult(change_x, xt)
    term1 = H
    term2 = m.scalar_mult(1 / v.dot(gamma,change_x),m.matrix_mult(gamma, gammat))
    term3 = m.scalar_mult(1 / v.dot(m.matrix_mult(xt,H),change_x),m.matrix_mult(H,m.matrix_mult(xxt, H)))
    print(term1, term2, term3)
    return m.matrix_add(term1, m.matrix_add(term2, m.scalar_mult(-1, term3)))

print(hessian(H4,gamma4,change_x4))