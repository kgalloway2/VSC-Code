import vector_functions as v
import matrix_functions as m
import csv

x, B, a, d, y = [], [], [], [], []

x.append([[-3], [1]])
B.append([[1,0],[0,1]])
tolerance = 5 * 10 ** -5

def f(xf):
    x1 = xf[0][0]
    x2 = xf[1][0]
    return (x1 ** 2) - (2 * x2 * x1 ** 2) + 4 * (x2 ** 2)

def grad_f(xg):
    x1 = xg[0][0]
    x2 = xg[1][0]
    return [[2 * x1 - 2 * x2],[-2 * x1 + 8 * x2]]

def alphak(x, d):
    x1 = x[0][0]
    x2 = x[1][0]
    d1 = d[0][0]
    d2 = d[1][0]
    num = -d1 * (x1 - x2) + d2 * (x1 - 4 * x2)
    den = (d1 ** 2) - 2 * d1 * d2 + 4 * (d2 ** 2)
    return num / den

a.append(alphak(x[0], v.scalar_mult(-1, grad_f(x[0]))))                       #a0
x.append(v.vector_add(x[0], v.scalar_mult(-a[0],grad_f(x[0]))))             #x1
y.append(v.vector_add(grad_f(x[1]), v.scalar_mult(-1, grad_f(x[0]))))        #y0
d.append(v.vector_add(x[1], v.scalar_mult(-1, x[0])))                      #d0
print(f(x[0]))

def BFGSupdate(B, y, d):
    ydt = v.vector_mult(y, v.transpose(d))
    dyt = v.vector_mult(d, v.transpose(y))
    dty = v.dot(v.transpose(d), y)
    ddt = v.vector_mult(d, v.transpose(d))
    term2 = m.scalar_mult(-1 / dty, m.matrix_add(m.matrix_mult(B, ydt), m.matrix_mult(dyt, B)))
    ytBinvy = v.dot(v.transpose(y), m.matrix_mult(B, y))
    term3 = m.scalar_mult((1 + (ytBinvy / (dty * dty))), ddt)
    return m.matrix_add(B, m.matrix_add(term2, term3))

B.append(BFGSupdate(B[0], y[0], d[0]))              #B1

print([0, x[0], d[0], a[0], f(x[0])])

with open('midterm_7.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    k = 1
    while True and k < 10000:
        d.append(m.scalar_mult(-1, m.matrix_mult(B[k], grad_f(x[k]))))
        a.append(alphak(x[k], d[k]))
        inc = v.scalar_mult(a[k],d[k])
        x.append(v.vector_add(x[k], inc))
        data_writer.writerow([k, x[k], d[k], a[k], f(x[k]),abs(f(x[k]) - f(x[k - 1]))])
        y.append(v.vector_add(grad_f(x[k]), v.scalar_mult(-1, grad_f(x[k - 1]))))
        B.append(BFGSupdate(B[k], y[k], d[k]))
        k += 1
        if abs(f(x[k]) - f(x[k - 1])) <= tolerance:
            print('tolerance reached')
            break

print(x[k-1], f(x[k-1]))
print([k, x[k],f(x[k]),abs(f(x[k]) - f(x[k - 1]))])