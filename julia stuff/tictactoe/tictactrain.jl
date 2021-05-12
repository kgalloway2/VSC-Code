using LinearAlgebra
# an input is a 9x1 vector with entries correspoding to the board positions from left to right top to bottom
# 0 is empty, -1 is O, and 1 is X
# the board XOO
#           OXO
#           X  
# is represented by [1, -1, -1, -1, 1, -1, 1, 0, 0]
# the best outcome in this case would be [0, 0, 0, 0, 0, 0, 0, 0, 1]
# winning the game

training_input = [[1, -1, -1, -1, 1, -1, 1, 0, 0]]
training_target = [[0, 0, 0, 0, 0, 0, 0, 0, 1]]

# the source I looked at (https://nestedsoftware.com/2019/12/27/tic-tac-toe-with-a-neural-network-1fjn.206436.html)
# used 36 nodes in each of two hidden layers
# they are randomly initialized

h1_weights = rand(36, 9)    # weight matrices for hidden layer 1
h2_weights = rand(36, 36)    # weight matrices for hidden layer 2
final_weights = rand(9, 36)   # weight matrices for final layer

tolerance = 10 ^ -6         # tolerance for difference between output and target
alpha = 0.1                 # size of step for gradient descent
N = length(training_input)  # number of data input and output

h1_num_nodes = 36           # number of nodes in h1
h1_inputs = []              # initialize hidden layer inputs
h1_outputs = []             # initialize hidden layer outputs
for i in 1:h1_num_nodes     # fill hidden units with 0s
    push!(h1_inputs, 0)
    push!(h1_outputs, 0)
end

h2_num_nodes = 36           # number of nodes in h2
h2_inputs = []              # initialize hidden layer inputs
h2_outputs = []             # initialize hidden layer outputs
for i in 1:h2_num_nodes     # fill hidden units with 0s
    push!(h2_inputs, 0)
    push!(h2_outputs, 0)
end
n = length(training_input[1])    # dimensionality of input/number of input units
m = length(training_target[1])    # dimensionality of output

final_layer_in = []         # initialize output layer inputs
final_layer_out = []        # initialize output layer outputs
errors = []                 # initialize errors

for i in 1:m      
    push!(final_layer_in, 0)    
    push!(final_layer_out, 0)   # fill output units with 0s
    push!(errors, 0)            # fill errors with 0s
end

new_h1_weights = zeros(Float64, (36, 9))             # make empty lists to fill with new weights later
new_h2_weights = zeros(Float64, (36, 36))             # make empty lists to fill with new weights later
new_final_weights = zeros(Float64, (9, 36))           # make empty lists to fill with new weights later


# now define the bipolar sigmoid used for gradient descent between each layer and error function
    
function f(x)
    return 1 / (1 + Base.MathConstants.e ^ (-x))
end

function f_prime(x)
    return (1 - f(x)) * f(x)
end

function error_function(actual, guess)
    diffs = actual - guess
    squares = (diffs).^2
    errors = 0.5 * squares
    return sum(errors)
end

# algorithm
graph_pairs = []
current_error = 0                           # initialize error
k = -1                                      # initialize interation counter
iterations = 0
while (true)
    global k = (k + 1) % N + 1
    global current_error
    global iterations
    if (k == 1)                                 # this if block was for getting coordinate pairs to graph the learning
        iterations += 1
        if (iterations % 10 == 0)
            push!(graph_pairs, (iterations, current_error))
        end
    end
    
    # input layer to hidden layer 1
    global h1_weights
    global h1_inputs = h1_weights * training_input[k]   # apply weights to input
    global h1_outputs = f.(h1_inputs)                   # apply activation function

    # hidden layer 1 to hidden layer 2
    global h2_weights
    global h2_inputs = h2_weights * h1_outputs             
    global h2_outputs = f.(h2_inputs)

    # hidden layer to output layer
    global final_weights
                              
    global final_layer_in = final_weights * h2_outputs                
    global final_layer_out = f.(final_layer_in)
    temp_error = error_function(training_target[k], final_layer_out)
    current_error += temp_error


    if (k == 1)                                          # check learning progress or quit if too many iterations
        if (current_error < tolerance || iterations >= 100000)
            break
        end
        current_error = 0
    end

    # backpropagation part of the algorithm

    # find changes for weights for hidden layer 2 to output layer
    changes_final_weights = zeros(9,36)
    delta_final_weights = zeros(m)
    for b in 1:m
        delta_final_weights[b] =  -(training_target[k][b] - final_layer_out[b]) * f_prime(final_layer_in[b])
        for j in 1:h2_num_nodes
            changes_final_weights[b,j] = alpha * delta_final_weights[b] * h2_outputs[j]
        end
    end

    # find changes for weights from hidden 1 to hidden 2
    changes_layer2_weights = zeros(36,36)
    delta_layer2_weights = zeros(36)
    for g in 1:h2_num_nodes
        delta_layer2_weights[g] = delta_final_weights[1,1] * final_weights[1, g] * f_prime(h2_inputs[g])
        for b in 1:h1_num_nodes
            changes_layer2_weights[g,b] = alpha * delta_layer2_weights[g] * h1_outputs[b]
        end
    end

    # find changes for weights for input to hidden
    changes_layer1_weights = zeros(36,n)
    delta_layer1_weights = zeros(36)
    for j in 1:h1_num_nodes
        temp = (delta_layer2_weights[1,1] * h2_weights[1,j] + delta_layer2_weights[2,1] * h2_weights[2,j])
        delta_layer1_weights[j] = temp * f_prime(h1_inputs[j])
        for b in 1:n
            changes_layer1_weights[j,b] = alpha * delta_layer1_weights[j,1] * training_input[k][b]
        end
    end
    
    # accumulate new changes
    # global new_h1_weights
    # display(new_h1_weights)
    # display(changes_layer1_weights)
    global new_h1_weights += changes_layer1_weights
    global new_h2_weights += changes_layer2_weights
    global new_final_weights += changes_final_weights

    # find new weights
    if (k == 1)
        h1_weights -= new_h1_weights
        h2_weights -= new_h2_weights
        final_weights -= new_final_weights
    end
end

final_outputs = []
for c in 1:length(training_input)
    # input layer to hidden layer 1
    h1_inputs = h1_weights * training_input[c]
    h1_outputs = f.(h1_inputs)

    # hidden layer 1 to hidden layer 2
    h2_inputs = h2_weights * h1_outputs
    h2_outputs = f.(h2_inputs)

    # hidden layer to output layer 
    final_layer_in = final_weights * h2_outputs
    push!(final_outputs, f.(final_layer_in))

end

temp_error = 0
for i in 1:length(training_target)
    global temp_error += error_function(training_target[k], final_outputs[k])
end
       

println("final output: ", final_outputs, "\nfinal error: ",temp_error, "\niterations: ",iterations)        