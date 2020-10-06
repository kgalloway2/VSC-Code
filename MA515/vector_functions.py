vector_1 = [1, 2, 3, 4, 5, 6, 7]
vector_2 = [0, -3, 5, -2, -6, 3, 0]
vector_3 = [[1], [2], [-1], [-2], [3], [-3], [4]]
scalar_1 = -1
scalar_2 = 0.5

def vector_add(v, w):
    if len(v) != len(w):
        raise Exception("Vectors are not the same size.")
    sum_vector = []
    if type(v[0]) == type(w[0]):
        if type(v[0]) == list:
            for i in range(len(v)):
                sum_vector.append([v[i][0] + w[i][0]])
        else:
            for i in range(len(v)):
                sum_vector.append(v[i] + w[i])
    else:
        if type(v[0]) == list:
            for i in range(len(v)):
                sum_vector.append([v[i][0] + w[i]])
        else:
            for i in range(len(v)):
                sum_vector.append(v[i] + w[i][0])
    return sum_vector

def vector_mult(v, w):
    if len(v) != len(w):
        raise Exception("Vectors are not the same size.")
    if (type(v[0]) is float or type(v[0]) is int) and (type(w[0]) is float or type(w[0]) is int):
        product_vector = []
        for i in range(len(v)):
            product_vector.append(v[i] * w[i])
        return product_vector
    product_vector = []
    if type(v[0]) == list:
        for i in range(len(v)):
            current_row = []
            for j in range(len(w)):
                current_row.append(v[i][0] * w[j])
            product_vector.append(current_row)
        return product_vector
    else:
        product_vector = 0
        for i in range(len(v)):
            product_vector += (v[i] * w[i][0])
        return [product_vector]

def dot(v,w):
    if len(v[0]) == len(w):
        product = 0
        for i in range(len(v[0])):
            product += (v[0][i] * w[i][0])
        return product
    if len(v) != len(w):
        raise Exception("Vectors are not the same size.")
    if (type(v[0]) is float or type(v[0]) is int): # row vectors
        product = 0
        for i in range(len(v)):
            product += (v[i] * w[i])
    else: #column vectors  
        product = 0
        for i in range(len(v)):
            product += (v[i][0] * w[i][0])
    return product

def transpose(v):
    v_t = []
    if type(v[0]) == list:
        v_t.append([])
        for i in v:
            v_t[0].append(i[0])
        return v_t
    else:
        for i in range(len(v)):
            v_t.append([v[i]])
        return v_t

def scalar_mult(c, v):
    if type(v) != list or (type(c) != float and type(c) != int):
        raise Exception('Cannot multiply these. Check input.')
    product = []
    if type(v[0]) != list:
        for i in range(len(v)):
            product.append(c * v[i])
    else:
        for i in range(len(v)):
            product.append([c * v[i][0]])
    return product

def euc_norm(v):
    norm2 = 0
    if type(v[0]) == list:
        for i in range(len(v)):
            norm2 += v[i][0] ** 2
    else:
        for i in range(len(v)):
            norm2 += v[i] ** 2
    return norm2 ** 0.5