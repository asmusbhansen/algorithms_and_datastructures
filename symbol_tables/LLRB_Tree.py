# Left linked Red-Black tree
from binary_search_tree import Node, BinarySearchTree

import numpy as np


class LLRBTree(BinarySearchTree):

    def flip_colors(self, h):

        h.color = 'red'
        h.left.color = 'black'
        h.right.color = 'black'

    def rotate_left(self, h):

        #x = h.right
        x = Node(key=h.right.key, 
                 val=h.right.val, 
                 count=h.right.count, 
                 left=h.right.left, 
                 right=h.right.right, 
                 color=h.right.color)

        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 'red'
        x.count = h.count
        h.count = 1 + self.size_(h.left)+ self.size_(h.right)

        return x

    def rotate_right(self, h):

        x = Node(key=h.left.key, 
                 val=h.left.val, 
                 count=h.left.count, 
                 left=h.left.left, 
                 right=h.left.right, 
                 color=h.left.color)

        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 'red'
        x.count = h.count
        h.count = 1 + self.size_(h.left)+ self.size_(h.right)

        return x

    def is_red(self, x):

        if x is None:
            return False

        return x.color == 'red'

    def put(self, key, val):
        self.root = self.put_(self.root, key, val)
        self.root.color = 'black'
        print(f'Put - Root: {self.root.to_string()}')

    def put_(self, x, key, val):

        if x is None:
            return Node(key=key, val=val, count=1, color='red')
        
        x = self.put_cmp(x, key, val)

        x.count = self.size_(x.left) + self.size_(x.right) + 1

        if self.is_red(x.right) and self.is_red(x.left) == False:
            print(f'Rotating left')
            x = self.rotate_left(x)

        if self.is_red(x.left) and self.is_red(x.left.left):
            print(f'Rotating right')
            x = self.rotate_right(x)

        if self.is_red(x.right) and self.is_red(x.left):
            print(f'Flip')
            self.flip_colors(x)

        

        return x

llrbt = LLRBTree()

arr = np.array([3, 4, 2])

for val, key in zip(arr, arr):
    print(f'Key: {key}, val: {val}')

    llrbt.put(key, val)
    print(f'BST Valid? {llrbt.is_bst()}')
