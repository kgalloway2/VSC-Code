import math

a = 6
b = 8
r = 0
tolerance = 10 ** -6

def f(x):
    return (2 - math.log(x)) / x

def bisector(a, b, r, tolerance, f):
    mid = (a + b) / 2
    if ((abs(a - b) / abs(a))< tolerance) and (abs(f(mid)) < tolerance):
        print(mid)
    else:
        if f(a) * f(mid) < 0:
            bisector(a, mid, r, tolerance, f)
        else:
            bisector(mid, b, r, tolerance, f)

bisector(a, b, r, tolerance, f)