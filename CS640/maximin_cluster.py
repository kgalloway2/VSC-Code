data = [[1,1],[2,2],[10,11],[6,1],[10,10],[6,4]]
n = len(data)

distances = []

def avg_cluster_distance():
    temp_sum = 0
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            temp_sum += distances[centers[i]][centers[j]]
    return temp_sum / len(centers)

for i in data:
    distances.append([])
    for j in data:
        distance = ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5
        distances[-1].append(distance)

centers = []
max_dist = -1
for i in range(n):
    for j in range(n):
        if distances[i][j] > max_dist:
            max_dist = distances[i][j]
            centers = [i,j]

while True:
    temp_distances = []
    for i in range(n):
        cur_min = float('inf')
        if i not in centers:
            for j in centers:
                if distances[i][j] < cur_min:
                    cur_min = distances[i][j]
                    temp = (j,i,cur_min)
            temp_distances.append(temp)

    new_center = max(temp_distances, key=lambda x: x[2])

    if new_center[2] >= 0.5 * avg_cluster_distance():
        break
    else:
        centers.append(new_center[0])

clusters = []
for i in range(n):
    cur_min = float('inf')
    if i not in centers:
        for j in centers:
            if distances[i][j] < cur_min:
                cur_min = distances[i][j]
                temp = (data[i],j)
    else:
        temp = (data[i], i)
    clusters.append(temp)

clusters.sort(key=lambda tup: tup[1])
print(clusters)