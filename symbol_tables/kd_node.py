import numpy as np

class kDNode:

    def __init__(self, key=None, left=None, right=None, val=None, count=0, color='black', level=0):

        self.key = key
        self.val = val
        self.count = count
        self.left = left
        self.right = right
        self.color = color
        self.level = level
        self.k = len(self.key)

    def get_k_idx(self):

        return self.level % self.k

    def compare_to(self, key_other):

        if self.key.shape != key_other.shape:
            print(self.key, key_other)
            print(self.key.shape, key_other.shape)
            assert False
            
        k_idx = self.get_k_idx()

        print(f'Comparing {self.key} to {key_other}, idx {k_idx}')

        key_temp = self.key[k_idx]
        key_other_temp = key_other[k_idx]

        # If keys are equal
        if np.all(np.equal(self.key, key_other)):
            return 0
        # If self key is less than input key - Put right 
        elif key_temp < key_other_temp:
            return -1
        # If self key is equal to input key - Put right
        elif key_temp == key_other_temp:
            return -1
        # Put left
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

        return f'key = {self.key}, left key = {lkey}, right key = {rkey}, color = {self.color}, level = {self.level}'
    