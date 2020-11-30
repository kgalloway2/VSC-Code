def f(t,y):
    return y - (t ** 2) + 1

ys = [1/2]
interval = [0,2]
delta_t = 0.2

ts = [interval[0]]
for j in range(int(interval[1] / 0.2)):
    ts.append(ts[-1] + delta_t)

for i in range(len(ts)):
    K1 = delta_t * f(ts[i],ys[i])
    K2 = delta_t * f(ts[i] + delta_t, ys[i] + K1)
    ys.append(ys[i] + (1/2) * (K1 + K2))

print(ys)