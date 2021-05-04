import guassian as g

data = [(2,2),(4,3),(6,1),(8,3),(10,2)]
k = len(data)

'''based on newton lagrange mtehod from page 108. worked on example he did.'''

matrix = []

for i in range(k):
    matrix.append([1])
    prev_entry = 1
    for j in range(1, k):
        if j > i:
            matrix[i].append(0)
        else:
            entry = (data[i][0] - data[j - 1][0]) * prev_entry
            matrix[i].append(entry)
            prev_entry = entry
    matrix[i].append(data[i][1])

for i in matrix:
    print(i)

print(g.gelim(matrix))