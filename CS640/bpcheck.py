import math
import vector_functions as v 
import matrix_functions as m 

# initial data, parameters, functions

training_in = [[[1],[2],[4]]]     # column vectors, already augmented
training_out = [[[1],[-1]]]     #note it needs to be bipolar sigmoid to be able to achieve a value of -1
v_weights = [[[0.2],[0.1],[-0.1]]]   # one column vector [bias, v11,v21]t
w_weights = [[[-0.2],[-0.1]],[[0.2],[0.1]]]     # two column vectors [bias, w11]t, [bias,w12]t
tolerance = 10 ** -6
alpha = 1
N = len(training_in)       # number of data input and output
Yin = []                   # initialize output layer inputs
y = []                     # initialize output layer outputs
e = []                     # initialize errors
h = 1                      # number of hidden layers
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

k = -1
iterations = 0
while True:
    k = (k + 1) % N
    if k == 0:
        iterations += 1
    
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
    
    if error < tolerance or iterations >= 10000:
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
    for i in range(h):
        changes_v.append([])
        delta_v.append([(delta_w[0][0] * w_weights[0][1][0] + delta_w[1][0] * w_weights[1][1][0]) * f_prime(Zin[i])])  # don't include bias weight
        for b in range(m + 1):
            if b == 0:
                changes_v[i].append(alpha * delta_v[i][0])
            else:
                changes_v[i].append(alpha * delta_v[i][0] * training_in[k][b][0])

    # find new weights
    for i in range(len(w_weights)):
        w_weights[i] = v.vector_add(w_weights[i], v.scalar_mult(-1, changes_w[i]))
    for i in range(len(v_weights)):
        v_weights[i] = v.vector_add(v_weights[i], v.scalar_mult(-1, changes_v[i]))

print(w_weights,'\n',v_weights,'\n',y, error, iterations)