

x = [0.5,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50]
y = [0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]
w = [0.5,0.5]
alpha = 0.002

N = len(x)

def h(k):
    return w[0] + w[1] * x[k]

def gradh(k, w):
    if w == 0:
        return 2 * (h(k) - y[k])
    else:
        return 2 * (h(k) - y[k]) * x[k]

def J():
    result = 0
    for i in range(N):
        result += (h(i) - y[i]) ** 2
    return result

def Jtrain():
    result = 0
    for i in range(N):
        result += (w[0] + w[1] * x[i] - y[i]) ** 2
    return result

iterations = 0
print('initial J', J())
print('initial Jtrain',Jtrain())
while J() > 1 and iterations < 500:
    grad0 = 0
    grad1 = 0
    for i in range(N):
        grad0 += gradh(i,0)
        grad1 += gradh(i,1)
    w[0] -= alpha * grad0
    w[1] -= alpha * grad1
    if iterations % 50 == 0:
        print('iteration',iterations,w)
        print('current J:', J(), 'current Jtrain:',Jtrain())
    iterations += 1

print(iterations, w, 'current J:', J(), 'current Jtrain:',Jtrain())