data = [(2, 2, 4),(3, 2, 20),(2, 3, 15),(3, 3, 25)]
h, k = data[3][0] - data[0][0], data[3][1] - data[0][1] 
x1, y1 = data[0][0], data[0][1]

if (data[1][0] != x1 + h) or (data[1][1] != y1) or (data[2][1] != y1 + k) or (data[2][0] != x1):
    print('Not a rectangle. Cannot interpolate.')
else:
    f1, f2, f3, f4 = data[0][2], data[1][2], data[2][2], data[3][2]
    a = f1
    b = (f2 - f1) / h
    c = (f3 - f1) / k
    d = (f4 + f1 - f2 - f3) / (h * k)
    print(a,'+', b, '(x - (',x1,'))+',c,'(y - (',y1,'))+', d,'(x - (',x1,'))','(y - (',y1,'))')