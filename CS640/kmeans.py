data = [[1,1],[2,2],[10,11],[6,1],[10,10],[6,4]]
K = 3
n = len(data)

def dist(p,q):
    distance = ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5
    return distance

means = []
for i in range(K):
    means.append(data[i])

changed = True
while changed:
    clusters = []
    for i in data:
        cur_min = float('inf')
        if i not in means:
            for j in means:
                distance = dist(i,j)
                if distance < cur_min:
                    cur_min = distance
                    temp = (i,means.index(j))
        else:
            temp = (i, means.index(i))
        clusters.append(temp)

    changed = False
    for m in range(K):
        temp_vec = [0,0]
        count = 0
        for p in clusters:
            if p[1] == m:
                temp_vec[0] = temp_vec[0] + p[0][0]
                temp_vec[1] = temp_vec[1] + p[0][1]
                count += 1
        temp_vec[0] = temp_vec[0] / count
        temp_vec[1] = temp_vec[1] / count
        if temp_vec != means[m]:
            means[m] = temp_vec
            changed = True


print(means)
print(clusters)