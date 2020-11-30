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
    K2 = delta_t * f(ts[i] + delta_t / 2, ys[i] + K1 / 2)
    K3 = delta_t * f(ts[i] + delta_t / 2, ys[i] + K2 / 2)
    K4 = delta_t * f(ts[i] + delta_t, ys[i] + K3)
    ys.append(ys[i] + (1/6) * (K1 + 2 * K2 + 2 * K3 + K4))

print(ys)