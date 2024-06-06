import numpy as np
import sys
sys.path.insert(0, r'C:/source/algorithms_and_datastructures/sort_helpers') 
from sort_helpers import time_sort, is_sorted

def exch(l, i, j):
    li = l[i]
    lj = l[j]
    if li > lj:
        l[i] = lj
        l[j] = li

def sort(l):
    count = 0
    #while(is_sorted(l) == False):
    for i in range(l.shape[0]):
        for j in range(l.shape[0]):
            if i < j:
                exch(l, i, j)
                #print(f'l: {l}')
            count += 1

    print(f'Iterations: {count}, iterations / N = {count / l.shape[0]:.4f}')

    return l
arr = np.random.randint(0,10,10)
arr = np.array([5,9,1,8,7,0,3,6,2,4])

arr_sorted = sort(arr)
assert is_sorted(arr_sorted)


time_sort(sort, sort_kwargs={}, duplicates=True, start=3, stop=13, tests=2)