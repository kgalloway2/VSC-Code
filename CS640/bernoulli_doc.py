
'''works based on example from page 162. needs some work to generalize.'''

class_1 = [[1,0,0,0,1,1,1,1],
[0,0,1,0,1,1,0,0],
[0,1,0,1,0,1,1,0],
[1,0,0,1,0,1,0,1],
[1,0,0,0,1,0,1,1],
[0,0,1,1,0,0,1,1]]
class_2 = [[0,1,1,0,0,0,1,0],
[1,1,0,1,0,0,1,1],
[0,1,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,1,0,1,0]]

document = [1,0,0,1,1,1,0,1]

p_class_1 = len(class_1) / (len(class_1) + len(class_2))
p_class_2 = len(class_2) / (len(class_1) + len(class_2))

sd_class_1 = class_1[0]
for i in class_1[1:]:
    for j in range(len(i)):
        sd_class_1[j] += i[j]

sd_class_2 = class_2[0]
for m in class_2[1:]:
    for n in range(len(m)):
        sd_class_2[n] += m[n]

for i in range(len(sd_class_1)):
    sd_class_1[i] /= len(class_1)
    sd_class_2[i] /= len(class_2)

def p_xi_c1(i):
    term1 = document[i] * sd_class_1[i]
    term2 = (1 - document[i]) * (1 - sd_class_1[i])
    return term1 + term2

def p_xi_c2(i):
    term1 = document[i] * sd_class_2[i]
    term2 = (1 - document[i]) * (1 - sd_class_2[i])
    return term1 + term2

p_c1_x = p_class_1
for i in range(len(document)):
    p_c1_x *= p_xi_c1(i)

p_c2_x = p_class_2
for j in range(len(document)):
    p_c2_x *= p_xi_c2(j)

print(p_c1_x, p_c2_x)
