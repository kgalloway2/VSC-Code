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

def alphak(xa, da):
    x1 = xa[0][0]
    x2 = xa[1][0]
    d1 = da[0][0]
    d2 = da[1][0]
    num = -100 * d2 * (x2 - x1) + d1 * ( 100 * x2 - 101 * x1 + 1)
    den = 100 * (d2 **2) - 200 * d1 * d2 + 101 * (d1 **2)
    return num / den

d = [v.scalar_mult(-1, grad_f(x[0]))]     # initialize list of d with d0
a = [alphak(x[0], d[0])]                    # initialize list of a with a0

d.append(d[0])
x.append(v.vector_add(x[0], v.scalar_mult(a[0], d[0])))    # add x1 to x

print([0,x[0],a[0],d[0],f(x[0])])

with open('hw2p2b.csv',mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    k = 1
    while abs(f(x[-1]) - f(x[-2])) > tolerance and k < 10000:
        d.append(v.scalar_mult(-1, grad_f(x[k])))
        a.append(alphak(x[-1], d[-1]))
        x.append(v.vector_add(x[-1], v.scalar_mult(a[-1], d[-1])))
        data_writer.writerow([k,x[-1],a[-1],d[-1],f(x[-1]),abs(f(x[-1]) - f(x[-2]))])
        k += 1

print(x[k - 1], f(x[k - 1]))
print(x[k], f(x[k]), k, abs(f(x[k]) - f(x[k - 1])))