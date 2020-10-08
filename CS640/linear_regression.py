

x = [23, 26, 30, 34]
y = [651, 762, 856, 1073]
w = [120,15]
alpha = 0.01

def h(k):
    return w[0] + w[1] * x[k]

def gradh(k, w):
    if w == 0:
        return 2 * (h(k) - y[k])
    else:
        return 2 * (h(k) - y[k]) * x[k]

def J():
    result = 0
    for i in range(4):
        result += (h(i) - y[i]) ** 2
    return result

iterations = 0
print('initial J', J())
while iterations < 4:
    grad0 = 0
    grad1 = 0
    for i in range(4):
        grad0 += gradh(i,0)
        grad1 += gradh(i,1)

    w[0] -= alpha * grad0
    w[1] -= alpha * grad1
    print(w, 'current J', J())
    iterations += 1