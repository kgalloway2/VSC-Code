import collections
import math

"""This program creates a decision tree for data pased on the attributes of the data. 
It currently works with categorical and quantitative attributes. It returns a preorder list of the decision tree."""


training_data = [
    ['Sunny', 'Hot', 'High', 'False', 'No'],
    ['Sunny', 'Hot', 'High', 'True', 'No'],
    ['Overcast', 'Hot', 'High', 'False', 'Yes'],
    ['Rainy', 'Mild', 'High', 'False', 'Yes'],
    ['Rainy', 'Cool', 'Normal', 'False', 'Yes'],
    ['Rainy', 'Cool', 'Normal', 'True', 'No'],
    ['Overcast', 'Cool', 'Normal', 'True', 'Yes'],
    ['Sunny', 'Mild', 'High', 'False', 'No'],
    ['Sunny', 'Cool', 'Normal', 'False', 'Yes'],
    ['Rainy', 'Mild', 'Normal', 'False', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'True', 'Yes'],
    ['Overcast', 'Mild', 'High', 'True', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'False', 'Yes'],
    ['Rainy', 'Mild', 'High', 'True', 'No']
]

orig_entropy = 0
outcomes = collections.Counter(j[-1] for j in training_data)
den = sum(outcomes.values())
entropy = 0
for j in outcomes.values():
    orig_entropy -= (j / den) * math.log((j / den), 10)

def recursive(dataset, used_attributes):
    if not dataset:
        print('stop1')
        return None
    if len(collections.Counter(j[-1] for j in dataset)) == 1:
        print('stop3', 'classify as', dataset[0][-1])
        return None
    if len(used_attributes) == (len(dataset[0]) - 1):                 # these are the termination conditions
        print('stop2', 'likely need more attibutes')
        return None

    max_info_gain = 0
    for i in range(len(dataset[0]) - 1): # checks each attribute of a data vector, -1 to not include the respondent
        if i not in used_attributes:
            if type(dataset[0][i]) is str:
                cur_attr_values = collections.Counter([j[i] for j in dataset])
                partitions = {}
                for k in cur_attr_values.keys():
                    partitions[k] = []
                for m in dataset:
                    partitions[m[i]].append(m)
                weighted_entropy = 0
                for n in partitions:
                    outcomes = collections.Counter(j[-1] for j in partitions[n])
                    den = sum(outcomes.values())
                    entropy = 0
                    for j in outcomes.values():
                        entropy -= (j / den) * math.log((j / den), 10)
                    weighted_entropy += entropy * len(partitions[n]) / len(dataset)
                cur_info_gain = orig_entropy - weighted_entropy
                if cur_info_gain >= max_info_gain:
                    max_info_gain = cur_info_gain
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
                    weighted_entropy = 0
                    for r in range(2):
                        outcomes = collections.Counter(j[-1] for j in partitions[h][r])
                        den = sum(outcomes.values())
                        entropy = 0
                        for j in outcomes.values():
                            entropy -= (j / den) * math.log((j / den), 10)
                        weighted_entropy += entropy * len(partitions[h][r]) / len(dataset)
                    cur_info_gain = orig_entropy - weighted_entropy
                    if cur_info_gain >= max_info_gain:
                        max_info_gain = cur_info_gain
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
