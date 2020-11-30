data = [[1,1],[2,2],[10,11],[6,1],[10,10],[6,4]]
T = 4

checked = [(data[0], 0)]
data.pop(0)
last_cluster = 0

for i in data:
    cur_min = float('inf')
    cur_cluster = -1
    for j in checked:
        distance = ((i[0] - j[0][0]) ** 2 + (i[1] - j[0][1]) ** 2) ** 0.5
        if distance < T and distance < cur_min:
            cur_min = distance
            cur_cluster = j[1]
    if cur_cluster == -1:
        cur_cluster = last_cluster + 1
        last_cluster += 1
    checked.append((i,cur_cluster))
    
checked.sort(key=lambda tup: tup[1])
print(checked)