import math

'''Finds the min of 1d functions.'''

phi = ((5 ** 0.5) - 1) / 2

a = 0
b = 2
d = phi * (b - a)
x1 = a + d
x2 = b - d

tolerance = 10 ** -3

def f(x):
    return (x ** 4) - (14 * (x ** 3)) + (60 * (x ** 2)) - (70 * x)

def golden(a, b, x1, x2, tolerance, f):
    print((a,b,x1,x2,abs(a-b)))
    if (abs(a - b) < tolerance):
        x = (b + a) / 2
        print(x, f(x))
    else:
        if f(x1) < f(x2):
            a = x2
            b = b
            d = phi * (b - a)
            x1 = a + d
            x2 = b - d
            golden(a,b,x1,x2, tolerance, f)
        else:
            a = a
            b = x1
            d = phi * (b - a)
            x1 = a + d
            x2 = b - d
            golden(a,b,x1,x2, tolerance, f)

golden(a, b, x1, x2, tolerance, f)