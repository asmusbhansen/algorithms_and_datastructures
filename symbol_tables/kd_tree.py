from kd_node import kDNode
from binary_search_tree import BinarySearchTree
import numpy as np
from tqdm import tqdm
import time
import matplotlib.pyplot as plt

class kdTree(BinarySearchTree):

    def __init__(self):
        self.node = kDNode

    def put(self, key, val):
        level = 0
        self.root = self.put_(self.root, key, val, level)
        self.root.color = 'black'
        #print(f'Put - Root: {self.root.to_string()}')

    # Only level increase is changed from BST implementation
    def put_(self, x, key, val, level):

        if x is None:
            x = self.node(key=key, val=val, count=1, level=level)
            #print(f'Inserting: {x.to_string()}')
            return x
        
        x = self.put_cmp(x, key, val, level)

        x.count = self.size_(x.left) + self.size_(x.right) + 1

        #print(f'put_: {x.to_string()}')

        return x


    def put_cmp(self, x, key, val, level):

        cmp = x.compare_to(key)

        #print(f'Node key {x.key}, new key {key}, level: {level}, cmp {cmp}')

        level += 1

        if cmp < 0:
            #print(f'Put right')
            x.right = self.put_(x.right, key, val, level)
        elif cmp > 0:
            #print(f'Put left')
            x.left = self.put_(x.left, key, val, level)
        # If keys are equal - Overwrite val
        else:
            x.val = val
            
        return x

    def range_search(self, key_min, key_max):

        points = []
        return self.range_search_(self.root, key_min, key_max, points)

    def range_search_(self, x, key_min, key_max, points):

        if x is None:
            return points

        # If x is within range, add to points
        in_range = True
        
        for n, key_ in enumerate(x.key):
            if key_min[n] > x.key[n] or key_max[n] < x.key[n]:
                in_range = False
                break

        if in_range:
            print(f'Search match: {x.to_string()}')
            points += [x]
            


        #Check for maximum of search range
        cmp_max = x.compare_to(key_max)

        #Check for minimum of search range
        cmp_min = x.compare_to(key_min)

        # If both max and min key is below, search only left sub-tree
        if cmp_max > 0 and cmp_min > 0:
            print(f'key_min {key_min} and key_max {key_max}, smaller than node key {x.key} at idx {x.level%x.k} - Searching only left')
            points = self.range_search_(x.left, key_min, key_max, points)

        # If max and min key is above, search right sub-tree
        elif cmp_max < 0 and cmp_min < 0:
            print(f'key_min {key_min} and key_max {key_max}, larger than node key {x.key} at idx {x.level%x.k} - Searching only right')
            points = self.range_search_(x.right, key_min, key_max, points)

        # Search both sub-trees
        else:
            print(f'key_min {key_min} and key_max {key_max}, surrounds node key {x.key} at idx {x.level%x.k} - Searching both trees')
            points = self.range_search_(x.left, key_min, key_max, points)
            points = self.range_search_(x.right, key_min, key_max, points)

        print(f'Points at node {x.to_string()}')
        for point in points:
            print(point.to_string())

        return points



#arr = [np.array([1, 1]),
#       np.array([1, 3]),
#       np.array([1, 2])]

#key_min=np.array([0, 0])
#key_max=np.array([10, 10])

min_int = 0
max_int = 10
dim = 2

arr = np.random.randint(min_int, max_int, size=(4, dim))
print(f'Arr: {arr}')

kd_tree = kdTree()

for val, key in zip(arr, arr):
        #print(f'Key: {key}, val: {val}')
        
        kd_tree.put(key, val)

vals_1 = np.random.randint(min_int, max_int, dim)
vals_2 = np.random.randint(min_int, max_int, dim)
key_min = np.minimum(vals_1, vals_2)
key_max = np.maximum(vals_1, vals_2)


points = kd_tree.range_search(key_min, key_max)

print(f'key_min: {key_min}')
print(f'key_max: {key_max}')
print(f'Search found points:')
for point in points:
    print(point.to_string())
'''
tests = 1000

ls = []
ts = []

for i in tqdm(range(tests)):

    kd_tree = kdTree()

    points = np.random.randint(5, tests)
    dim = np.random.randint(2, tests)
    arr = np.random.randint(low=0, high=points, size=(points, dim))
    #print(f'arr: {arr}')

    time_start = time.time()

    for val, key in zip(arr, arr):
        #print(f'Key: {key}, val: {val}')
        
        kd_tree.put(key, val)
        

    for key in arr: 
        val = kd_tree.get(key)
        #print(f'Get - Key: {key}, val: {val}')
        assert np.all(np.equal(key, val))
        
    ls += [points]
    ts += [time.time()-time_start]

plt.figure()
plt.scatter(ls, ts, alpha=0.1, label='Time spent in tree')
plt.legend()
#plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Time')
plt.show()

        

#print(f'LLRBTree Size: {kd_tree.size()}')
#print(f'LLRBTree Min: {kd_tree.min()}')
#print(f'LLRBTree Max: {kd_tree.max()}')
#print(f'LLRBTree Keys: {kd_tree.keys()}')
'''