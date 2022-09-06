import numpy as np

class Node:

    key = None
    val = None
    left = None
    right = None
    count = 0

    def __init__(self, key=None, val=None, count=None):

        self.key = key
        self.val = val
        self.count = count

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

        return f'key = {self.key}, left key = {lkey}, right key = {rkey}'
    

class BinarySearchTree:

    root = None

    def size(self):
        return self.size(self.root)

    def size_(self, x):
        if x is None:
            return 0
        else:
            return x.count

    def get(self, key):
        return self.get_(self.root, key)

    def get_(self, x, key):

        if x is None:
            return None

        cmp = x.compare_to(key)

        # If x is less than key - Get left
        if cmp < 0:
            print(f'New key {key} less than node key {x.key} - Get right')
            self.get_(x.right, key)
        elif cmp > 0:
            print(f'New key {key} larger than node key {x.key} - Get left')
            self.get_(x.left, key)
        else:
            return x.val

    def put(self, key, val):
        self.root = self.put_(self.root, key, val)

    def put_(self, x, key, val):
        print(f'put_ - x: {x}')
        if x is None:
            return Node(key=key, val=val, count=1)
        
        cmp = x.compare_to(key)

        # If x is less than key - Put left
        if cmp < 0:
            print(f'Node key {key} less than new key {x.key} - Put right')
            x.right = self.put_(x.right, key, val)
        elif cmp > 0:
            print(f'Node key {key} larger than new key {x.key} - Put left')
            x.left = self.put_(x.left, key, val)
        # If keys are equal - Overwrite val
        else:
            x.val = val
        x.count = self.size_(x.left) + self.size_(x.right) + 1

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


bst = BinarySearchTree()

arr = np.array([3, 2, 4, 1, 2.5])

for val, key in zip(arr, arr):
    print(f'Key: {key}, val: {val}')

    bst.put(key, val)
    print(f'BST Valid? {bst.is_bst()}')
