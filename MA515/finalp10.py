import math
import vector_functions as v

def f(t,y):
    return [[((math.e ** (2 * t)) * math.sin(t)) + 2 * y[0][0] -2 * y[1][0]],
            [y[0][0]]]

ys = [[[-0.4],[-0.6]]]
interval = [0,0.2]
delta_t = 0.1

ts = [interval[0]]
for j in range(int(interval[1] / 0.2)):
    ts.append(ts[-1] + delta_t)

for i in range(len(ts)):
    K1 = v.scalar_mult(delta_t,f(ts[i],ys[i]))
    K2 = v.scalar_mult(delta_t,f(ts[i] + delta_t, v.vector_add(ys[i],K1)))
    ys.append(v.vector_add(ys[i], v.scalar_mult(0.5, v.vector_add(K1, K2))))

for y in ys:
    print(y)