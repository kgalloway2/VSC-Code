tolerance = 10 ** -6
previous = 0
current = 0.5

def g(x):
    return (0.5) * 3 ** (-x)

while abs(previous - current) > tolerance:
    previous = current
    current = g(current)

print(current, g(current))