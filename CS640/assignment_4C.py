import math
import vector_functions as v 
import matrix_functions as m 
import csv

# initial data, parameters, functions

training_in = [[[1],[-1],[-1]], 
                [[1],[-1],[1]],
                [[1],[1],[-1]],
                [[1],[1],[1]]]     # column vectors, already augmented
training_out = [[[-1]],
                [[1]],
                [[1]],
                [[-1]]]   
v_weights = [[[0.07],[0.2],[-0.3]],
                [[-0.06],[0.4],[0.25]],
                [[0.09],[-0.1],[-0.5]]]   #column vector [bias(v0j), v1j,v2j]t to jth hidden unit, initializing all randomly
v2_weights = [[[0.03],[-0.3],[0.18],[-0.45]],
                [[-0.04],[-0.3],[-0.25],[-0.4]]]    #column vector [bias(v0j), v1j,v2j,v3j]t to jth hidden unit, initializing all randomly
w_weights = [[[-0.05],[0.1],[0.1]]]  #column vector [bias(w01), w11, w21]t to 1st (only) output unit, initializing all randomly
tolerance = 10 ** -4
alpha = 1
N = len(training_in)       # number of data input and output
Yin = []                   # initialize output layer inputs
y = []                     # initialize output layer outputs
e = []                     # initialize errors
h1 = 3                      # number of hidden units
Zin1 = []                   # initialize hidden layer inputs
z1 = []                     # initialize hidden layer outputs
for i in range(h1):         # fill hidden units with 0s
    Zin1.append(0)
    z1.append(0)
h2 = 2                      # number of hidden units
Zin2 = []                   # initialize hidden layer inputs
z2 = []                     # initialize hidden layer outputs
for i in range(h2):         # fill hidden units with 0s
    Zin2.append(0)
    z2.append(0)
n = len(training_in[0])    # dimensionality of input/number of input units
m = len(training_out[0])   # dimensionality of output
for i in range(m):      
    Yin.append(0)
    y.append(0)            # fill output units with 0s
    e.append(0)            # fill errors with 0s

def f(x):
    return (2 / (1 + math.e ** (-x))) - 1

def f_prime(x):
    return ((1 - f(x)) * (1 + f(x))) / 2

Z_v = []
Z_v2 = []
Z_w = []
for i in range(len(v_weights)):
    Z_v.append([[0],[0],[0]])
for i in range(len(v2_weights)):
    Z_v2.append([[0],[0],[0],[0]])
for i in range(len(w_weights)):
    Z_w.append([[0],[0],[0]])

# algorithm
graph_pairs = []
error = 0
k = -1
iterations = 0
while True:
    k = (k + 1) % N
    if k == 0:
        iterations += 1
        if iterations % 10 == 0:
            graph_pairs.append((iterations, error))
    
    # input layer to hidden layer 1
    for j in range(h1):
        Zin1[j] = v.dot(v_weights[j],training_in[k])            # should be a dot product that returns a scalar// [1] is the augment/bias
        z1[j] = [f(Zin1[j])]                                    # hidden unit j's output

    # hidden layer 1 to hidden layer 2
    for g in range(h2):
        Zin2[g] = v.dot(v2_weights[g],[[1]] + z1)               # [1] is the augment/bias
        z2[g] = [f(Zin2[g])]

    # hidden layer to output layer
    for b in range(m):                               
        Yin[b] = v.dot(w_weights[b],[[1]] + z2)                 # [1] is the augment/bias
        y[b] = f(Yin[b])
        e[b] = 0.5 * ((training_out[k][b][0] - y[b])  ** 2)     # errors
    error += sum(e)                                             # error is sum of errors of last four training vectors

    if k == 0:
        if error < tolerance or iterations >= 10000:
            break
        error = 0

    # find changes for weights for hidden2 to outputs
    changes_w = []
    delta_w = []
    for b in range(m):
        changes_w.append([])
        delta_w.append([-(training_out[k][b][0] - y[b]) * f_prime(Yin[b])])
        for j in range(h2 + 1):
            if j == 0:
                changes_w[b].append(alpha * delta_w[b][0])
            else:
                changes_w[b].append(alpha * delta_w[b][0] * z2[j - 1][0])

    # find changes for weights from hidden 1 to hidden 2
    changes_v2 = []
    delta_v2 = []
    for g in range(h2):
        changes_v2.append([])
        delta_v2.append([(delta_w[0][0] * w_weights[0][g][0]) * f_prime(Zin2[g])])
        for b in range(h1 + 1):
            if b == 0:
                changes_v2[g].append(alpha * delta_v2[g][0])
            else:
                changes_v2[g].append(alpha * delta_v2[g][0] * z1[b - 1][0])
    
    # find changes for weights for input to hidden
    changes_v = []
    delta_v = []
    for j in range(h1):
        changes_v.append([])
        temp = (delta_v2[0][0] * v2_weights[0][j][0] + delta_v2[1][0] * v2_weights[1][j][0])
        delta_v.append([temp * f_prime(Zin1[j])])
        for b in range(n):
            if b == 0:
                changes_v[j].append(alpha * delta_v[j][0])
            else:
                changes_v[j].append(alpha * delta_v[j][0] * training_in[k][b][0])
    
    # accumulate new changes
    for i in range(len(v_weights)):
        Z_v[i] = v.vector_add(Z_v[i], changes_v[i])
    for i in range(len(v2_weights)):
        Z_v2[i] = v.vector_add(Z_v2[i], changes_v2[i])
    for i in range(len(w_weights)):
        Z_w[i] = v.vector_add(Z_w[i], changes_w[i])

    # find new weights
    if k == 0:
        for i in range(len(v_weights)):
            v_weights[i] = v.vector_add(v_weights[i], v.scalar_mult(-1, Z_v[i]))
            Z_v[i] = [[0],[0],[0]]
        for i in range(len(v2_weights)):
            v2_weights[i] = v.vector_add(v2_weights[i], v.scalar_mult(-1, Z_v2[i]))
            Z_v2[i] = [[0],[0],[0],[0]]
        for i in range(len(w_weights)):
            w_weights[i] = v.vector_add(w_weights[i], v.scalar_mult(-1, Z_w[i]))
            Z_w[i] = [[0],[0],[0]]
        
print(v_weights)
print('---------------------')
print(v2_weights)
print('---------------------')
print(w_weights)
print('---------------------')

final_outputs = []
for x in training_in:
    # input layer to hidden layer 1
    for j in range(h1):
        Zin1[j] = v.dot(v_weights[j],x)            
        z1[j] = [f(Zin1[j])]                                   

    # hidden layer 1 to hidden layer 2
    for g in range(h2):
        Zin2[g] = v.dot(v2_weights[g],[[1]] + z1)
        z2[g] = [f(Zin2[g])]

    # hidden layer to output layer
    for b in range(m):                               
        Yin[b] = v.dot(w_weights[b],[[1]] + z2)                     
        final_outputs.append(f(Yin[b]))   

e_final = []
for i in range(len(training_out)):
    e_final.append(0.5 * ((final_outputs[i] - training_out[i][0][0])  ** 2))
error_final = sum(e_final)                                           

print(final_outputs, error_final, iterations)

with open('assignment_4C.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in graph_pairs:
        data_writer.writerow([i[0],i[1]])