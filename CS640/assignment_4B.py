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
v_weights = [[[-0.44],[0.23],[-0.31]],
                [[-0.12],[0.42],[0.22]],
                [[0.27],[0.09],[-0.15]],
                [[-0.18],[-0.39],[-0.23]]]   #column vector [bias(v0j), v1j,v2j]t to jth hidden unit, initializing all randomly
w_weights = [[[-0.11],[-0.4],[-0.16],[0.35],[0.02]]]  #column vector [bias(w01), w11, w21, w31, w41]t to 1st (only) output unit, initializing all randomly
tolerance = 10 ** -3
alpha = 1
N = len(training_in)       # number of data input and output
Yin = []                   # initialize output layer inputs
y = []                     # initialize output layer outputs
e = []                     # initialize errors
h = 4                      # number of hidden units
Zin = []                   # initialize hidden layer inputs
z = []                     # initialize hidden layer outputs
for i in range(h):         # fill hidden units with 0s
    Zin.append(0)
    z.append(0)
n = len(training_in[0])    # dimensionality of input/number of input units
m = len(training_out[0])   # dimensionality of output
for i in range(m):      
    Yin.append(0)
    y.append(0)            # fill output units with 0s
    e.append(0)            # fill errors with 0s

def f(x):
    return (2 / (1 + math.e ** (-x))) - 1

def f_prime(x):
    return (1 - f(x)) * (1 + f(x)) / 2

# algorithm
graph_pairs = []
error = -1
k = -1
iterations = 0
while True:
    k = (k + 1) % N
    if k == 0:
        iterations += 1
        graph_pairs.append((iterations, error))
    
    # input layer to hidden layer
    for j in range(h):
        Zin[j] = v.dot(v_weights[j],training_in[k])     # should be a dot product that returns a scalar// [1] is the augment/bias
        z[j] = [f(Zin[j])]                                    # hidden unit j's output

    # hidden layer to output layer
    for b in range(m):                                  
        Yin[b] = v.dot(w_weights[b],[[1]] + z)        # [1] is the augment/bias
        y[b] = f(Yin[b])
        e[b] = 0.5 * ((training_out[k][b][0] - y[b])  ** 2)                  # errors
    error = sum(e)                                         # error is sum of errors 

    if error < tolerance or iterations >= 500:
        break

    # find changes for weights for hidden to outputs
    changes_w = []
    delta_w = []
    for b in range(m):
        changes_w.append([])
        delta_w.append([-(training_out[k][b][0] - y[b]) * f_prime(Yin[b])])
        for j in range(h + 1):
            if j == 0:
                changes_w[b].append(alpha * delta_w[b][0])
            else:
                changes_w[b].append(alpha * delta_w[b][0] * z[j - 1][0])

    # find changes for weights for input to hidden
    changes_v = []
    delta_v = []
    for j in range(h):
        changes_v.append([])
        delta_v.append([(delta_w[0][0] * w_weights[0][j][0]) * f_prime(Zin[j])])  # only one delta_w since one output unit
        for b in range(n):
            if b == 0:
                changes_v[j].append(alpha * delta_v[j][0])
            else:
                changes_v[j].append(alpha * delta_v[j][0] * training_in[k][b][0])
    
    # find new weights
    for i in range(len(w_weights)):
        w_weights[i] = v.vector_add(w_weights[i], v.scalar_mult(-1, changes_w[i]))
    for i in range(len(v_weights)):
        v_weights[i] = v.vector_add(v_weights[i], v.scalar_mult(-1, changes_v[i]))

print(w_weights)
print(v_weights)

final_outputs = []
for x in training_in:
    for j in range(h):
        Zin[j] = v.dot(v_weights[j],x)
        z[j] = [f(Zin[j])]                                  

    # hidden layer to output layer
    for b in range(m):                                  
        Yin[b] = v.dot(w_weights[b],[[1]] + z)
        final_outputs.append(f(Yin[b]))

print(final_outputs, error, iterations)

with open('assignment_4B.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in graph_pairs:
        data_writer.writerow([i[0],i[1]])