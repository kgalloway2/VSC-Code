import vector_functions as v 
import matrix_functions as m 

'''works on two examples from class. very likely generalizable'''

matrix1 = [[1,1,1,0,0,40],
[4,1,0,1,0,100],
[-20,-10,0,0,1,0]]

matrix2 = [[2,3,2,1,0,0,1000],
[1,1,2,0,1,0,800],
[-7,-8,-10,0,0,1,0]]

def negative_in_obj(m):
    for i in m[-1]:
        if i < 0:
            return True
    return False

def most_negative(m):
    cur_min = float('inf')
    most_index = -1
    for i in range(len(m[-1])):
        if m[-1][i] < cur_min:
            cur_min = m[-1][i]
            most_index = i
    return most_index

def best_ratio(m,c):
    cur_ratio = float('inf')
    index = -1
    for i in range(len(m) - 1):
        ratio = m[i][-1] / m[i][c]
        if ratio < cur_ratio:
            cur_ratio = ratio
            index = i
    return index

def simplex1(matrix):
    while negative_in_obj(matrix):
        pivot_column = most_negative(matrix)
        pivot_row = best_ratio(matrix,pivot_column)
        matrix[pivot_row] = v.scalar_mult(1 / matrix[pivot_row][pivot_column],[matrix[pivot_row]])[0]
        for i in range(len(matrix)):
            if i != pivot_row:
                factor = matrix[i][pivot_column]
                matrix[i] = v.vector_add([matrix[i]], v.scalar_mult(-factor, [matrix[pivot_row]]))[0]

simplex1(matrix1)
    
for i in range(len(matrix1)):
    print(matrix1[i])