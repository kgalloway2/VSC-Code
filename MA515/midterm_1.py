'''just a test to check some stuff'''

a = [3]
b = [3.99]
c = [3]

iterations = 0
while abs(a[-1] - 4) > 0.0000001 and iterations < 100:
    temp = (1 / 4) * (8 * a[-1] - a[-1] ** 2)
    a.append(temp)
    iterations += 1

iterations = 0
while abs(b[-1] - 4) > 0.0000001 and iterations < 100:
    temp = (1 / 3) * ((b[-1] ** 2) - 4)
    b.append(temp)
    iterations += 1

iterations = 0
while abs(c[-1] - 4) > 0.0000001 and iterations < 100:
    temp = (3 * c[-1] + 4) ** 0.5
    c.append(temp)
    iterations += 1
print(a)
print(b)
print(c)