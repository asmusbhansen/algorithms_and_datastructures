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
        
        #for n, key_ in enumerate(x.key):
        #    if key_min[n] > x.key[n] or key_max[n] < x.key[n]:
        #        in_range = False
        #        break

        in_range = x.in_range(key_min, key_max)

        if in_range:
            #print(f'Search match: {x.to_string()}')
            points += [x]
            
        #Check for maximum of search range
        cmp_max = x.compare_to(key_max)

        #Check for minimum of search range
        cmp_min = x.compare_to(key_min)

        # If both max and min key is below, search only left sub-tree
        if cmp_max > 0 and cmp_min > 0:
            #print(f'key_min {key_min} and key_max {key_max}, smaller than node key {x.key} at idx {x.level%x.k} - Searching only left')
            points = self.range_search_(x.left, key_min, key_max, points)

        # If max and min key is above, search right sub-tree
        elif cmp_max < 0 and cmp_min < 0:
            #print(f'key_min {key_min} and key_max {key_max}, larger than node key {x.key} at idx {x.level%x.k} - Searching only right')
            points = self.range_search_(x.right, key_min, key_max, points)

        # Search both sub-trees
        else:
            #print(f'key_min {key_min} and key_max {key_max}, surrounds node key {x.key} at idx {x.level%x.k} - Searching both trees')
            points = self.range_search_(x.left, key_min, key_max, points)
            points = self.range_search_(x.right, key_min, key_max, points)

        #print(f'Points at node {x.to_string()}')
        #for point in points:
        #    print(point.to_string())

        return points

    def dist(self, key1, key2):
        return np.sqrt(np.sum((key1 - key2)**2))

    def update_current_best(self, key_node, search_key, current_best):
        
        if current_best is None:
            #print(f'-- Current best updated from {current_best} to {key_node} --')
            return key_node

        if self.dist(search_key, key_node) < self.dist(search_key, current_best):
            #print(f'- Current best updated from {current_best} to {key_node} --')
            return key_node
        else:
            return current_best
            
    def nearest_neighbour(self, search_key):

        current_best = None
        #print(f'Searching for Nearest Neighbour to search key: {search_key}')
        return self.nearest_neighbour_down(self.root, search_key, current_best, path=[])

    def nearest_neighbour_down(self, x, search_key, current_best, path):

        if x is None:
            return current_best

        path += [x]

        cmp = x.compare_to(search_key)

        #print(f'Down - Comparing node key {x.key} to search key {search_key}, idx {x.level%x.k}, cmp: {cmp}')

        # If key is less - Go down left subtree
        if cmp > 0:
            current_best = self.nearest_neighbour_down(x.left, search_key, current_best, path)
        
        # If key is larger - Go down right subtree
        elif cmp < 0:
            current_best = self.nearest_neighbour_down(x.right, search_key, current_best, path)
        # If key is equal - Update current best
        else:
            path = [] 

        # Update current best
        current_best = self.update_current_best(x.key, search_key, current_best)

        # Go up the path
        current_best = self.nearest_neighbour_up(search_key, current_best, path)

        return current_best

    def nearest_neighbour_up(self, search_key, current_best, path):
        
        if path == []:
            return current_best

        #print(f'Up path:')
        #for p in path:
        #    print(p.to_string())
        
        node = path[-1]

        # If the distance between the current best and key is less than current best and splitting plane, there is no need to go down other three
        key_idx = node.level % node.k
        search_other = self.dist(current_best, search_key) > np.abs(node.key[key_idx] - search_key[key_idx])
        #print(f'Search other: {self.dist(current_best, search_key)}, {np.abs(node.key[key_idx] - search_key[key_idx])}')

        #print(f'Up - Comparing node key {node.key}, search key {search_key} and best {current_best}, idx {node.level%node.k}. Search other? {search_other}')

        # Is current best in the left or right half of three?
        cmp = node.compare_to(search_key)
        #print(f'Up - cmp: {cmp}')
        # Current best is in left
        if cmp > 0:
            if search_other:
                #print(f'Up - Going down right')
                current_best = self.nearest_neighbour_down(node.right, search_key, current_best, path=[])
        # Current best is in Right
        elif cmp < 0:
            if search_other:
                #print(f'Up - Going down left')
                current_best = self.nearest_neighbour_down(node.left, search_key, current_best, path=[])

        # Remove current node from path
        path = path[:-1]
        #print(f'Down - New path len: {len(path)}')

        current_best = self.nearest_neighbour_up(search_key, current_best, path)

        return current_best

        
        

def find_min(arr, search_key):
    diff = arr - search_key
    dist = np.sqrt(np.sum(diff**2, axis=1))

    dist_argmin = np.argmin(dist)

    return arr[dist_argmin, :] 
    

#arr = np.array([[0, 1],
#                [-1, 3],
#                [1, 2]])
'''
arr = np.array([[6, 3],
                [2, 8],
                [9, 5],
                [0, 5],
                [1, 8],
                [7, 3],
                [0, 6],
                [8, 2],
                [9, 1],
                [1, 3]])

search_key = np.array([6, 9])
'''
arr = np.array([[8, 0],
                [3, 2],
                [6, 5],
                [2, 2],
                [3, 1],
                [1, 8],
                [9, 6],
                [2, 5],
                [2, 4],
                [7, 3]])

search_key = np.array([0, 5])

tests = 100
dim = 2
min_points = 10000
max_points = 100000

ts = []
ts_naive = []
ls = []

for t in tqdm(np.arange(tests)):

    # Nearest neighbour test
    kd_tree = kdTree()

    for val, key in zip(arr, arr):
            
            kd_tree.put(key, val)

    #print(f'\n\n ---- Test {t} ---- ')
    points = np.random.randint(min_points, max_points)
    arr = np.random.uniform(0, 1, size=(points, dim))
    search_key = np.random.uniform(0, 1, dim)

    #search_key = np.array([1,2.1])

    time_start = time.time()
    true_find = find_min(arr, search_key)
    ts_naive += [time.time() - time_start]
    

    time_start = time.time()
    search_find = kd_tree.nearest_neighbour(search_key)
    ts += [time.time() - time_start]
    ls += [points]
    

    true_dist = np.sqrt(np.mean((search_key-true_find)**2))
    find_dist = np.sqrt(np.mean((search_key-search_find)**2))

    success = find_dist <= true_dist 

    #print(f'search_key: {search_key}')
    #print(f'search_find: {search_find}, {find_dist}')
    #print(f'true_find: {true_find}, {true_dist}')
    

    if False:#success == False:
        #print(f'search_find: {search_find}')
        #print(f'arr:\n{arr}')
        plt.figure()
        plt.scatter(arr[:,0], arr[:,1])
        plt.scatter(search_key[0], search_key[1], label='Search key', s=200, alpha=0.3)
        plt.scatter(true_find[0], true_find[1], label='True find', s=100, alpha=0.3)
        plt.scatter(search_find[0], search_find[1], label='Search find', s=50)
        plt.legend()

        plt.ylim(-0.1,1.1)
        plt.xlim(-0.1,1.1)
        plt.title(f'Success {success}')
        plt.show()    

    assert success


plt.figure()
plt.scatter(ls, ts_naive, alpha=0.1, label='Naive Nearest Neighbour')
plt.scatter(ls, ts, alpha=0.1, label='kD Tree Nearest Neighbour')
plt.legend()
plt.xlabel('N')
plt.ylabel('Time')
#plt.yscale('log')
plt.show()

# Range search test
'''
tests = 10
min_num_points = 1000
max_num_points = 100000
min_int = 0
max_int = max_num_points - min_num_points
dim = 2

PLOT = False
EVAL = False

ts = []
ls = []

for i in tqdm(range(tests)):
    #print(f'\n\n ---- Test {i} ---- ')
    num_points = np.random.randint(min_num_points, max_num_points)
    dim = np.random.randint(min_int, max_int)
    arr = np.random.randint(min_int, max_int, size=(num_points, dim))
    #print(f'arr: {arr}')
    kd_tree = kdTree()

    for val, key in zip(arr, arr):
            
            kd_tree.put(key, val)

    key_min = np.random.randint(min_int, max_int-1, dim)
    key_max = np.zeros(dim)
    for i in range(key_max.shape[0]):
        key_max[i] = np.random.randint(key_min[i]+1, max_int)

    #key_min = np.minimum(vals_1, vals_2)
    #key_max = np.maximum(vals_1, vals_2)
    print(f'key_min: {key_min}')
    print(f'key_max: {key_max}')

    time_start = time.time()
    points = kd_tree.range_search(key_min, key_max)
    ts += [time.time() - time_start]
    ls += [num_points]

    if EVAL:
        points_test = []
        for n in range(arr.shape[0]):
            node = kDNode(key=arr[n, :])
            if node.in_range(key_min, key_max):
                points_test += [node]


        found_same = len(points) == len(points_test)
        assert found_same
        
        for point in points:
            found = False
            for point_ in points_test:
                if np.all(np.equal(point.key, point_.key)):
                    found = True
                    break

            assert found
            
          
    if PLOT:

        plt.figure()

        ys = np.array([key_min[1], key_max[1], key_max[1], key_min[1], key_min[1]])#)
        xs = np.array([key_min[0], key_min[0], key_max[0], key_max[0], key_min[0]])#)

        plt.plot(xs, ys, color='blue')

        for n in range(arr.shape[0]):

            plt.scatter(arr[n, 0], arr[n, 1], color='black')

        for point in points:
            key = point.key
            plt.scatter(key[0], key[1], color='red')

        plt.title(f'# Found {len(points)}, # Test {len(points_test)}, # Total {arr.shape[0]}, Test {i+1}/{tests}')

    plt.show()


plt.figure()
plt.scatter(ls, ts, alpha=0.1, label='Time spent searching')
plt.legend()
plt.xlabel('N')
plt.ylabel('Time')
plt.show()
'''

# kD Tree test
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