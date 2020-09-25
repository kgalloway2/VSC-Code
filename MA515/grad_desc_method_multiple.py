import csv

w_0 = 0
w_1 = 1
w_2 = -1
a = 0.1
W = [w_0, w_1, w_2]
training_data = [
    [[-1, 1], 3],
    [[1, -1], -1],
    [[1, 1], 1],
    [[2, 1], 0],
    [[1, 2], 2]
]

def grad_0():
    result = 0
    for i in range(len(training_data)):
        result += W[0] + (W[1] * training_data[i][0][0]) + (W[2] * training_data[i][0][1]) - training_data[i][1]
    return 2 * result

def grad_1():
    result = 0
    for i in range(len(training_data)):
        result += (W[0] + (W[1] * training_data[i][0][0]) + (W[2] * training_data[i][0][1]) - training_data[i][1]) * training_data[i][0][0]
    return 2 * result

def grad_2():
    result = 0
    for i in range(len(training_data)):
        result += (W[0] + (W[1] * training_data[i][0][0]) + (W[2] * training_data[i][0][1]) - training_data[i][1]) * training_data[i][0][1]
    return 2 * result

def J(W):
    result = 0
    for i in range(len(training_data)):
        result += (W[0] + (W[1] * training_data[i][0][0]) + (W[2] * training_data[i][0][1]) - training_data[i][1]) ** 2
    return result

with open('assignment_1_data_multiple.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    count = 0
    while count < 1000 and J(W) != 0:    
        W[0] = W[0] - a * grad_0()
        W[1] = W[1] - a * grad_1()
        W[2] = W[2] - a * grad_2()
        data_writer.writerow([count + 1, J(W), W[0], W[1], W[2]])
        count += 1
