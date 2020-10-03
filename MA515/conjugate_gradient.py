import vector_functions as v
import matrix_functions as m
import csv

x = [[[-1.2],[1]]]              # initialize list of x with x0
tolerance = 5 * 10 ** -5

def f(xf):
    x1 = xf[0][0]
    x2 = xf[1][0]
    return (100 * ((x2 - x1) ** 2)) + ((1 - x1) ** 2)

def grad_f(xg):
    x1 = xg[0][0]
    x2 = xg[1][0]
    return [[-200 * (x2 - x1) - 2 * (1 - x1)],[200 * (x2 - x1)]]

def alphak(xa, sa):
    x1 = xa[0][0]
    x2 = xa[1][0]
    s1 = sa[0][0]
    s2 = sa[1][0]
    num = -100 * s2 * (x2 - x1) + s1 * ( 100 * x2 - 101 * x1 + 1)
    den = 100 * (s2 **2) - 200 * s1 * s2 + 101 * (s1 **2)
    return num / den

def get_B(gB, prevg):
    num = v.euc_norm(gB)
    den = v.euc_norm(prevg)
    return num / den

s = [v.scalar_mult(-1, grad_f(x[0]))]     # initialize list of s with s0
a = [alphak(x[0], s[0])]                    # initialize list of a with a0
B = [1]                                  # initialize empty list of B
g = []                                  # initialize empty list of g
print(a)

s.append(s[0])
x.append(v.vector_add(x[0], v.scalar_mult(a[0], s[0])))    # add x1 to x
g.append(v.scalar_mult(-1, grad_f(x[0])))           # add g0 to g

print([0,x[0],a[0],s[0],f(x[0])])

with open('hw2p2a.csv',mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    k = 1
    while abs(f(x[-1]) - f(x[k - 1])) > tolerance and k < 10000:
        g.append(v.scalar_mult(-1, grad_f(x[-1])))
        B.append(get_B(g[-1], g[-2])) 
        s.append(v.vector_add(g[-1], v.scalar_mult(B[-1], s[-1])))
        a.append(alphak(x[-1], s[-1]))
        x.append(v.vector_add(x[-1], v.scalar_mult(a[-1], s[-1])))
        data_writer.writerow([k,x[-1],a[-1],s[-1],f(x[-1]),abs(f(x[-1]) - f(x[k - 1]))])
        k += 1

print(x[k - 1], f(x[k - 1]))
print(x[k], f(x[k]), k, abs(f(x[k]) - f(x[k - 1])))