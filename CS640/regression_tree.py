import collections

"""This program creates a regression tree for data pased on the attributes of the data. 
It currently works with categorical and quantitative attributes. It returns a preorder list of the regression tree."""

training_data = [
    ['Sunny', 'Hot', 'High', 'False', 25],
    ['Sunny', 'Hot', 'High', 'True', 30],
    ['Overcast', 'Hot', 'High', 'False', 46],
    ['Rainy', 'Mild', 'High', 'False', 45],
    ['Rainy', 'Cool', 'Normal', 'False', 52],
    ['Rainy', 'Cool', 'Normal', 'True', 23],
    ['Overcast', 'Cool', 'Normal', 'True', 43],
    ['Sunny', 'Mild', 'High', 'False', 35],
    ['Sunny', 'Cool', 'Normal', 'False', 38],
    ['Rainy', 'Mild', 'Normal', 'False', 46],
    ['Sunny', 'Mild', 'Normal', 'True', 48],
    ['Overcast', 'Mild', 'High', 'True', 52],
    ['Overcast', 'Hot', 'Normal', 'False', 44],
    ['Rainy', 'Mild', 'High', 'True', 30]
]

tolerance = 6

def std_dev(dataset, population):
    if len(dataset) == 1:
        return 0
    values = []
    for i in dataset:
        values.append(i[-1])
    mean = sum(values) / len(values)
    squared_deviations = []
    for j in values:
        squared_deviations.append((j - mean) ** 2)
    if population:
        den = len(dataset)
    else:
        den = len(dataset) - 1
    variance = sum(squared_deviations) / den
    std_dev = variance ** 0.5
    return std_dev

orig_std_dev = std_dev(training_data, True)

def recursive(dataset, used_attributes):
    if not dataset:
        print('stop1')
        return None
    if len(dataset) == 1:
        print('stop3', 'classify as', dataset[0][-1])
        return None
    if std_dev(dataset, False) <= tolerance:
        print('stop4 classify as', (sum(j[-1] for j in dataset) / len(dataset)))
        return None
    if len(used_attributes) == (len(dataset[0]) - 1):                 # these are the termination conditions
        print('stop2', 'likely need more attibutes')
        return None

    max_std_red = 0
    for i in range(len(dataset[0]) - 1): # checks each attribute of a data vector, -1 to not include the respondent
        if i not in used_attributes:
            if type(dataset[0][i]) is str:
                cur_attr_values = collections.Counter([j[i] for j in dataset])
                partitions = {}
                for k in cur_attr_values.keys():
                    partitions[k] = []
                for m in dataset:
                    partitions[m[i]].append(m)
                weighted_std_dev = 0
                for k in partitions:
                    cur_std_dev = std_dev(partitions[k], False)
                    weighted_std_dev += cur_std_dev * len(partitions[k]) / len(dataset)
                cur_std_red = orig_std_dev - weighted_std_dev
                if cur_std_red >= max_std_red:
                    max_std_red = cur_std_red
                    use_partition = partitions
                    attribute = i
            else:      #this attribute is non-categorical data, i.e., real number
                sorted_values = []
                for p in dataset:
                    if p[i] not in sorted_values:
                        sorted_values.append(p[i])
                sorted_values.sort()
                split_values = [(sorted_values[0] / 2)]
                for t in range(len(sorted_values) - 1):
                    split_values.append((sorted_values[t] + sorted_values[t + 1]) / 2)
                partitions = {}
                for k in split_values:
                    partitions[k] = [[],[]]
                for m in dataset:
                    for l in split_values:
                        if m[i] < l:
                            partitions[l][0].append(m)
                        else:
                            partitions[l][1].append(m)
                for h in partitions:
                    cur_std_dev = std_dev(h,False)
                    cur_std_red = orig_std_dev - cur_std_dev
                    if cur_std_red >= max_std_red:
                        max_std_red = cur_std_red
                        use_partition = {h : partitions[h]}
                        attribute = i
    print('new node for attribute', attribute)
    if type(dataset[0][attribute]) is str:
        for k in use_partition.values():    
            print('under', k[0][attribute], 'for attribute',attribute)
            recursive(k, (used_attributes + [attribute]))
    
    else:
        for k in use_partition.values():
            for b in k:
                if b == k[0]:
                    temp = 'less than'
                else:
                    temp = 'greater than'
                print('under', temp, use_partition.keys())
                recursive(b, (used_attributes + [attribute]))

print(recursive(training_data, []))