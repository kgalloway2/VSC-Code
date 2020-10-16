

x = [23, 26, 30, 34]
y = [651, 762, 856, 1073]
w = [120,15]
alpha = 0.0003

test_set = [[25,28,32],[690,800,950]]

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

def Jtrain():
    result = 0
    for i in range(3):
        result += (w[0] + w[1] * test_set[0][i] - test_set[1][i]) ** 2
    return result

iterations = 0
print('initial J', J())
print('initial Jtrain',Jtrain())
while J() > 2760:
    grad0 = 0
    grad1 = 0
    for i in range(4):
        grad0 += gradh(i,0)
        grad1 += gradh(i,1)
    w[0] -= alpha * grad0
    w[1] -= alpha * grad1
    if iterations % 200 == 0:
        print(w)
        print('current J:', J(), 'current Jtrain:',Jtrain())
    iterations += 1

print(iterations, w, 'current J:', J(), 'current Jtrain:',Jtrain())