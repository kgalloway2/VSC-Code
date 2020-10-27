import math

'''This finds roots. It requires two initial guesses. It approximates the derivative using a secant line.'''

x = [-2,-2.9]

def f(x):
    return 3 * (x ** 4) + 3 * (x ** 3) - 6 * (x ** 2) + 4

def f_prime(k):
    return (f(x[k]) - f(x[k - 1]) )/ (x[k] - x[k - 1])

x.append(x[1] - f(x[1]) / f_prime(1))

k = 2
while (abs(x[k] - x[k - 1]) >  (10 ** -3)):
    x.append(x[k] - f(x[k]) / f_prime(k))
    k += 1
    
print(x[-1], f(x[-1]))