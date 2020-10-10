vector_1 = [1, 2, 3, 4, 5, 6, 7]
vector_2 = [0, -3, 5, -2, -6, 3, 0]
vector_3 = [[1], [2], [-1], [-2], [3], [-3], [4]]
scalar_1 = -1
scalar_2 = 0.5

def vector_add(v, w):
    if len(v[0]) != len(w[0]):
        raise Exception("Vectors are not the same size.")
    sum_vector = []
    if len(v[0]) > 1: # 2 row vectors
        sum_vector.append([])
        for i in range(len(v[0])):
            sum_vector[0].append(v[0][i] + w[0][i])
    else: # 2 column vectors
        for i in range(len(v)):
            sum_vector.append([])
            sum_vector[i].append(v[i][0] + w[i][0])
    return sum_vector

def vector_mult(v, w):
    if len(v) == len(w) or len(v[0]) == len(w) or len(v) == len(w[0]):
        if (type(v[0]) is float or type(v[0]) is int) and (type(w[0]) is float or type(w[0]) is int):
            product_vector = []
            for i in range(len(v)):
                product_vector.append(v[i] * w[i])
            return product_vector
        
        if len(v[0]) > 1: # row * column
            product_vector = 0
            for i in range(len(v)):
                product_vector += (v[0][i] * w[i][0])
            return [product_vector]
            
        else: # column * row
            product_vector = []
            for i in range(len(v)):
                current_row = []
                for j in range(len(w[0])):
                    current_row.append(v[i][0] * w[0][j])
                product_vector.append(current_row)
            return product_vector
            
    else:
        raise Exception("Vectors are not the same size.")

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
    if type(v[0]) != list: # row vector
        product = [[]]
        for i in range(len(v)):
            product[0].append(c * v[i])
        return product[0]
    else:
        product = []
        for i in range(len(v)):
            product.append([c * v[i][0]])
    return product

def euc_norm(v):
    norm2 = 0
    if len(v[0]) > 1: # row vector
        for i in range(len(v)):
            norm2 += v[0][i] ** 2
    else:
        for i in range(len(v)): # column vector
            norm2 += v[i][0] ** 2
    return norm2 ** 0.5