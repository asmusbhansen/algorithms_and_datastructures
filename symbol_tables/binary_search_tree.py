import numpy as np
import time

class Node:

    def __init__(self, key=None, left=None, right=None, val=None, count=0, color='black'):

        self.key = key
        self.val = val
        self.count = count
        self.left = left
        self.right = right
        self.color = color

    def compare_to(self, key):
        
        if self.key < key:
            return -1
        elif self.key == key:
            return 0
        else:
            return 1

    def to_string(self):
        
        try:
            lkey = self.left.key
        except:
            lkey = None
        
        try:
            rkey = self.right.key
        except:
            rkey = None

        return f'key = {self.key}, left key = {lkey}, right key = {rkey}, color = {self.color}'
    

class BinarySearchTree:

    root = None
    time_put = 0
    puts = 0

    def depth(self):
        return self.depth_(self.root)

    def depth_(self, x):
        if x is None:
            return 1
        
        return np.max([self.depth_(x.left), self.depth_(x.right)]) + 1
    
    def size(self):
        return self.size_(self.root)

    def size_(self, x):
        if x is None:
            return 0
        else:
            return x.count

    def get(self, key):
        #print(f'get - key: {key}')
        return self.get_(self.root, key)

    def get_(self, x, key):

        if x is None:
            return None

        cmp = x.compare_to(key)

        #print(f'Node key {x.key}, get key {key}, cmp: {cmp}')

        # If x is less than key - Get left
        if cmp < 0:
            #print(f'Get right')
            return self.get_(x.right, key)
        elif cmp > 0:
            #print(f'Get left')
            return self.get_(x.left, key)
        else:
            #print(f'Return val: {x.val}')
            return x.val

    def contains(self, key):
        if self.get(key) is None:
            return False
        else:
            return True

    def put(self, key, val):
        #print(f'put - key: {key}, val: {val}')
        time_start = time.time()
        self.root = self.put_(self.root, key, val)
        self.time_put += time.time() - time_start
        self.puts += 1
        #print(f'time_put: {self.time_put}, puts: {self.puts}')

    def put_(self, x, key, val):
        
        if x is None:
            return Node(key=key, val=val, count=1)
        
        x = self.put_cmp(x, key, val)

        x.count = self.size_(x.left) + self.size_(x.right) + 1

        return x

    def put_cmp(self, x, key, val):

        cmp = x.compare_to(key)

        # If x is less than key - Put left
        #print(f'Node key {x.key}, new key {key}, cmp {cmp}')
        if cmp < 0:
            #print(f'Put right')
            x.right = self.put_(x.right, key, val)
        elif cmp > 0:
            #print(f'Put left')
            x.left = self.put_(x.left, key, val)
        # If keys are equal - Overwrite val
        else:
            x.val = val

        return x

    def is_bst(self):
        return self.is_bst_(self.root)

    def is_bst_(self, x):

        if x is None:
            return True

        print(f'Is BST - Node: {x.to_string()}')

        if x.left is not None and x.key < x.left.key:
            return False
        if x.right is not None and x.key > x.right.key:
            return False

        return self.is_bst_(x.left) and self.is_bst_(x.right)

    def keys(self):
        return self.keys_(self.root)

    def keys_(self, x):

        keys = [x.key]

        if x.left is not None:
            keys += self.keys_(x.left)

        if x.right is not None:
            keys += self.keys_(x.right)

        return keys

    def min(self):
        return self.min_(self.root)

    def min_(self, x):

        if x.left is None:
            return x.val
        else:
            return self.min_(x.left)

    def max(self):
        return self.max_(self.root)

    def max_(self, x):

        if x.right is None:
            return x.val
        else:
            return self.max_(x.right)


bst = BinarySearchTree()

arr = np.array([3, 2, 4, 1, 2.5, 5])

for val, key in zip(arr, arr):
    print(f'Key: {key}, val: {val}')

    bst.put(key, val)
    print(f'BST Valid? {bst.is_bst()}')

arr = np.array([3, 2, 4, 1, 2.5, 0.5, 5])

for key in arr: 
    val = bst.get(key)
    print(f'Get - Key: {key}, val: {val}')

print(f'BST Size: {bst.size()}')
print(f'BST Min: {bst.min()}')
print(f'BST Max: {bst.max()}')
print(f'BST Keys: {bst.keys()}')
