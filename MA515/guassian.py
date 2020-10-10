import vector_functions as v

'''seems to work with determined matrices'''

m1 = [[1,2,4,2],[2,-1,3,-3],[4,7,8,1]]
m2 = [[0.08701924763831913, 0.08935899685109217, 1.4, -0.008339749212773043],
[0.08935899685109217, 0.13914532913478955, 1.4, -0.01578633228369739],
[1.4, 1.4, 0, 0.02000000000000013]]


def gelim(m):
    coeff = [[]]
    for j in range(len(m) - 1):
        m[j] = v.scalar_mult(1 / m[j][j] , m[j])
        coeff.append([])
        for i in range(0, len(m)):
            if i != j:
                m[i] = v.vector_add([m[i]], [v.scalar_mult(-1 * m[i][j], m[j])])[0]
            

    coeff[-1] = (m[-1][-1] / m[-1][-2])

    for i in range(len(coeff) - 2, -1, -1):
        current = 0
        for j in range(len(coeff)):
            if type(coeff[j]) is not list:
                current += m[i][j] * coeff[j]
        coeff[i] = (m[i][-1] - current) / m[i][i]
    
    return coeff