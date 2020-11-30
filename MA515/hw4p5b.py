import math

'''based on assignment 4, problem 5'''

def f(t,y):
    return -y * math.log(y)

def y(t):
    return math.e ** (math.log(1/2) * math.e ** (-t))

delta_ts = [1/4,1/8,1/16,1/32, 1/64, 1/128]

for i in delta_ts:
    
    delta_t = i
    times = [0, delta_t]
    ys = [1/2, 1/2 + delta_t * f(delta_t,1/2)] # used forward euler to find y_1

    while times[-1] < 1:
        next_t = times[-1] + delta_t
        next_y = ys[-1] + (delta_t / 2) * (3 * f(times[-1], ys[-1]) - f(times[-2],ys[-2]))
        times.append(next_t)
        ys.append(next_y)

    actual_ys = []
    for j in times:
        actual_ys.append(y(j))

    errors = []    
    for i in range(len(ys)):
        errors.append(ys[i] - actual_ys[i])


    print('for delta_t =',delta_t)
    print('R_i=',max(errors))
    print('T_i=',max(errors) / delta_t)
    # for j in range(len(ys)):
    #     print((times[j],ys[j]))
    # print(actual_ys)
    print('------------------------------------------')