import math

'''This finds roots.'''

x = [1]

def f(x):
    return (x - 1) * x * (x + 1)

def f_prime(x):
    return x * (x + 1) + (x - 1) * ((x + 1) + x)

x.append(x[0] - f(x[0]) / f_prime(x[0]))

k = 1
while (abs(x[k] - x[k - 1]) >  (10 ** -3)):
    x.append(x[k] - f(x[k]) / f_prime(x[k]))
    k += 1
    
print(x[-1], f(x[-1]))