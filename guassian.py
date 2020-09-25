import vector_functions as v

m = [[1,2,4,2],[2,-1,3,-3],[4,7,8,1]]

def gelim(m):
    coeff = [[]]
    for j in range(len(m) - 1):
        m[j] = v.scalar_mult(1 / m[j][j] , m[j])
        coeff.append([])

        for i in range(0, len(m)):
            if i != j:
                m[i] = v.vector_add(m[i], v.scalar_mult(-1 * m[i][j], m[j]))


    coeff[-1] = (m[-1][-1] / m[-1][-2])

    for i in range(len(coeff) - 2, -1, -1):
        current = 0
        for j in range(len(coeff)):
            if type(coeff[j]) is not list:
                current += m[i][j] * coeff[j]
        coeff[i] = (m[i][-1] - current) / m[i][i]
    
    return coeff
