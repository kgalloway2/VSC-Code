m_1 = [[1,2,3],[4,5,6]]
m_2 = [[7,8,9],[10,11,12]]
m_3 = [[1,2,3],[4,6,6],[7,8,9]]
m_4 = [[2,2],[3,2]]

def size(m):
    if type(m[0]) is not list:
        n = 1
    else:
        n = len(m[0])
    return (len(m), n)

def transpose(m):
    transpose = []
    for j in range(len(m[0])):
        transpose.append([])
        for i in m:
            transpose[j].append(i[j])
    return transpose

def matrix_add(m, n):
    if size(m) != size(n):
        raise Exception('Matrices are not the same size. Cannot add.')
    answer = []
    for i in range(len(m)):
        answer.append([])
        for j in range(len(m[i])):
            answer[i].append(m[i][j] + n[i][j])
    return answer

def scalar_mult(c, m):
    answer = []
    for i in m:
        answer.append([])
        for j in i:
            answer[m.index(i)].append(j * c)
    return answer

def matrix_mult(m, n):
    if size(m)[1] != size(n)[0]:
        raise Exception('These matrices cannot be multiplied.')
    product = []
    for i in range(len(m)):
        product.append([])
        for k in range(len(n[0])):
            temp = 0
            for j in range(len(m[i])):
                temp += (m[i][j] * n[j][k])
            product[i].append(temp)
    return product

def minor(m, i, j):
    answer = []
    for k in range(len(m)):
        answer.append([])
        for b in range(len(m[k])):
            answer[k].append(m[k][b])
    for h in range(len(answer)):
        answer[h].pop(j)
    answer.pop(i)
    return answer

def determinant(m):
    if size(m)[0] != size(m)[1]:
        raise Exception('Not a square matrix. Cannot find determinant.')
    if size(m)[0] == 1:
        return m[0][0]
    elif size(m)[0] == 2:
        return (m[0][0] * m[1][1] - m[0][1] * m[1][0])
    else:
        result = 0
        for i in range(len(m[0])):
            if m[0][i] == 0:
                result += 0
            else:
                result += ((-1) ** i) * m[0][i] * determinant(minor(m,0,i))
        return result

def inverse(m):
    if len(m[0]) != 2 or len(m) != 2:
        raise Exception('Not a 2 x 2 matrix.')
    else:
        det = determinant(m)
        return scalar_mult(1 / det, [[m[1][1], -m[0][1]],[-m[1][0], m[0][0]]])