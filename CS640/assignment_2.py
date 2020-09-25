import random as r
import vector_functions as v
import math as m

def data_set(size):
    data = []
    count = 0
    while count < size:
        r1, theta1 = r.uniform(0,1), 6.28318 * r.random()            # generate random polar coordinates
        r2, theta2 = r.uniform(0,1) + 3, 6.28318 * r.random()        # then convert to rectangular
        data.append([1,r1 * m.cos(theta1), r1 * m.sin(theta1),1])    # [augment,x,y,class]
        data.append([1,r2 * m.cos(theta2), r2 * m.sin(theta2),2])    # 6.28318 to scale the angle to the entire circle
        count += 1
    return data

def f(vec):                 # this maps the data to a different pattern space
    vector = []
    for i in range(len(vec)):         # [augment,x,y,class] --> [augment,x,x^2,y,y^2,xy,class]
        if i == 0:
            vector.append(vec[i])
        elif i == len(vec) - 1:
            vector.append(vec[1] * vec[2])
            vector.append(vec[-1])
        else:
            vector.append(vec[i])
            vector.append(vec[i] ** 2)
    return vector

pre_training_pairs = data_set(50)
training_pairs = []


for i in pre_training_pairs:                  # map to a higher dimensional pattern space
    training_pairs.append(f(i))

initial_w = [0,0,0,0,0,0]                 # polynomial decision function with 6 parameters
alpha = 0.01
N = 100
n = 6

current_w = initial_w
k = 0
iterations = 0
changed = True
changes = 0


print('Before First Iteration, W =', current_w)

while (changed or k != 0) and iterations <= 500:
    current = v.vector_mult(current_w, v.transpose(training_pairs[k][:-1]))
    if k == 0:              # each time we return to the beginning, we reset things
        changed = False
        changes = 0
        z = [0,0,0,0,0,0]  

    if current[0] > 0:
        if training_pairs[k][-1] == 1:
            pass
        else:
            z = v.vector_add(z, v.scalar_mult(-1,training_pairs[k][:-1]))
            changed = True
            changes += 1
    else:
        if training_pairs[k][-1]  == 2:
            pass
        else:
            z = v.vector_add(z, v.scalar_mult(1,training_pairs[k][:-1]))
            changed = True
            changes += 1        
    
    k = (k + 1) % N

    if k == 0:        
        if changed == False:
            iterations += 1
            print('Final Iteration =', iterations, 'Misclassified =',changes, 'W =',current_w)
            break
        else:
            iterations += 1
            print('Iteration =', iterations, 'Misclassified =',changes, 'W =',current_w) # print current parameter vector and number of misclassified
            current_w = v.vector_add(current_w, v.scalar_mult(alpha, z))

'''for i in training_pairs:
    temp = v.vector_mult(current_w, v.transpose(i[:-1]))
    print(temp)
    if temp[0] > 0:
        print(i, "is in Class 1 and should be in Class", i[-1])
        if i[-1] == 1:
            print('Correct')
        else:
            print('Incorrect')
            incorrect += 1
    else:
        print(i, "is in Class 2 and should be in Class", i[-1])
        if i[-1] == 2:
            print('Correct')
        else:
            print('Incorrect')
            incorrect += 1'''

if iterations >= 500:
    print('Failed. Too many iterations before converging.')
    print('iteration', iterations, current_w, 'misclassified:',changes)