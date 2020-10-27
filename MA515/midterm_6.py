previous_1 = [0.5, 0.5]
iterations = 3

def f_1(x):
    return [(x[0] ** 2) + (x[1] ** 2) - 1, 5 * (x[0] ** 2) + 21 * (x[1] ** 2) - 9]

def grad_inv_1(x):
    a = 2 * x[0]
    b = 2 * x[1]
    c = 10 * x[0]
    d = 42 * x[1]
    det = (a * d) - (b * c)
    return [[(1 / det) * d, (-1 / det) * b], [(-1 / det) * c, (1 / det) * a]]

def mat_mult(a, b):
    return [a[0][0] * b[0] + a[0][1] * b[1], a[1][0] * b[0] + a[1][1] * b[1]]

def mat_sub(a, b):
    return [a[0] - b[0], a[1] - b[1]]

results = []
for i in range(iterations):
    print(grad_inv_1(previous_1))
    print(f_1(previous_1))
    print(mat_mult(grad_inv_1(previous_1),f_1(previous_1)))
    print('----------------')
    next_1 = mat_sub(previous_1, mat_mult(grad_inv_1(previous_1),f_1(previous_1)))
    previous_1 = next_1
    results.append(next_1)

print(results)