import vector_functions as v 
import matrix_functions as m 

matrix1 = [[1,3,2,1,0,0,10],
[1,5,1,0,1,0,8],
[-8,-10,-7,0,0,1,0]]

M = 10 ** 8
matrix2 = [[3,1,0,0,1,0,0,3],
            [4,3,-1,0,0,1,0,6],
            [1,2,0,1,0,0,0,3],
            [4 - 7 * M,1 - 4 * M,M,0,0,0,1,-9 * M]]

def negative_in_obj(m):
    for i in m[-1][:-1]:
        if i < 0:
            return True
    return False

def most_negative(m):
    cur_min = float('inf')
    most_index = -1
    for i in range(len(m[-1]) - 1):
        if m[-1][i] < cur_min:
            cur_min = m[-1][i]
            most_index = i
    return most_index

def best_ratio(m,c):
    cur_ratio = float('inf')
    index = -1
    for i in range(len(m) - 1):
        if m[i][c] == 0:
            pass
        else:
            ratio = m[i][-1] / m[i][c]
            if ratio <= cur_ratio:
                cur_ratio = ratio
                index = i
    return index

def simplex1(matrix):
    while negative_in_obj(matrix):
        pivot_column = most_negative(matrix)
        print('pivot column is',pivot_column)
        pivot_row = best_ratio(matrix,pivot_column)
        print('pivot row is',pivot_row)
        matrix[pivot_row] = v.scalar_mult(1 / matrix[pivot_row][pivot_column],[matrix[pivot_row]])[0]
        for i in range(len(matrix)):
            if i != pivot_row:
                factor = matrix[i][pivot_column]
                matrix[i] = v.vector_add([matrix[i]], v.scalar_mult(-factor, [matrix[pivot_row]]))[0]
        for i in range(len(matrix)):
            print(matrix[i])
        print('-----------------------------------------------------')

simplex1(matrix2)
    
for i in range(len(matrix2)):
    print(matrix2[i])