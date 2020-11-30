def f(t,y):
    return y - (t ** 2) + 1

ys = [1/2]
interval = [0,2]
delta_t = 0.2

ts = [interval[0]]
for j in range(int(interval[1] / 0.2)):
    ts.append(ts[-1] + delta_t)

for i in range(len(ts)):
    ys.append(ys[i] + delta_t * f(ts[i], ys[i]))

print(ys)