import random

counts = []
for k in range(1000000):
    r = 5
    g = 3
    count = 0

    while r != 0:
        if random.uniform(0,1) <= r / (r + g):
            r -= 1
        else:
            pass
        count += 1
    
    counts.append(count)

print(sum(counts) / 1000000)