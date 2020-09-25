import csv

w_0 = 2
w_1 = 1
a = 0.006
W = [w_0, w_1]
training_data = [[2, 5.1], [2.5, 5.9], [3.0, 7.1], [3.5, 7.9], [4.0, 9.1], [4.5, 9.9], [5.0, 11.1], [5.5, 12.0], [6.0, 13]]

def grad_1():
    result = 0
    for i in range(len(training_data)):
        result += W[0] + W[1] * training_data[i][0] - training_data[i][1]
    return 2 * result

def grad_2():
    result = 0
    for i in range(len(training_data)):
        result += (W[0] + W[1] * training_data[i][0] - training_data[i][1]) * training_data[i][0]
    return 2 * result

def J(W):
    result = 0
    for i in range(len(training_data)):
        result += (W[0] + W[1] * training_data[i][0] - training_data[i][1]) ** 2
    return result



with open('assignment_1_data.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    count = 0
    while J(W) > 0.1:    
        W[0] = W[0] - a * grad_1()
        W[1] = W[1] - a * grad_2()
        data_writer.writerow([count + 1, J(W), W[0], W[1]])
        count += 1
