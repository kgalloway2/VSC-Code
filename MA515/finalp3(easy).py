'''This is newton's method applied to find the minimum of a function. 
Like newton's method, it will return the min nearest to the initial guess.'''


x = [1]

def f(x):
    return (2 * (x ** 2)) - (4 * x) + 4

def f_prime(x):
    return 4 * x - 4

def f_prime2(x):
    return 4

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