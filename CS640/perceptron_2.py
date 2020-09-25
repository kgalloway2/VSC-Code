import vector_functions

training_pairs = [[1,72, 220], [1,74, 200], [-1,-60, -120], [-1,-63, -110]]           # N = 4, n = 2
Class_1 = training_pairs[:1]
Class_2 = training_pairs[2:]
initial_w = [-1000, 9, 4.8]                                                  # linear decision function with 3 parameters
alpha = 0.01
changed = True
N = 4
n = 2

current_w = initial_w
k = 0
iterations = 0

while (changed or k != 0) and iterations < 10 ** 5:
    current = vector_functions.vector_mult(current_w, vector_functions.transpose(training_pairs[k]))
    if k == 0:
        changed = False

    if current[0] > 0:
        current_w = current_w
    
    else:
        current_w = vector_functions.vector_add(current_w, vector_functions.scalar_mult(alpha, training_pairs[k]))
        changed = True
    
    k = (k + 1) % N

    if k == 0 and changed == False:
        break

    iterations += 1
    
print(current_w, iterations)

for i in training_pairs:
    temp = vector_functions.vector_mult(current_w, vector_functions.transpose(i))[0]

    if temp > 0 and i[0] == 1:
        print(i, "is in Class 1")
    else:
        print(i, "is in Class 2")

if iterations >= 10 ** 5:
    print('Failed. Too many iterations before converging.')