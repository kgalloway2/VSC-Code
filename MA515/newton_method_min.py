'''This is newton's method applied to find the minimum of a function. 
Like newton's method, it will return the min nearest to the initial guess.'''


x = [1]

def f(x):
    return (x - 1) * x * (x + 1)

def f_prime(x):
    return 3 * x ** 2 - 1

def f_prime2(x):
    return 6 * x

x.append(x[0] - f_prime(x[0]) / f_prime2(x[0]))

k = 1
while (abs(x[k] - x[k - 1]) >  (10 ** -3)):
    x.append(x[k] - f_prime(x[k]) / f_prime2(x[k]))
    k += 1
    
for i in range(len(x)):
    if i == 0:
        print(i, x[i],f(x[i]))
    else:
        print(i, x[i],f(x[i]), abs(f(x[i]) - f(x[i -1])))