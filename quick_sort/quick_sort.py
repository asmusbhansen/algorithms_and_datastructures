import numpy as np
import sys
sys.path.insert(0, r'C:/source/algorithms_and_datastructures/sort_helpers') 
from sort_helpers import time_sort, is_sorted

# Set recursion limit
sys.setrecursionlimit(10**6)

# THis implementation does not handle duplicate keys well - As the number of duplicate keys increase, the runtime goes to O(n^2)

def exch(l, i, j):
    li = l[i]
    lj = l[j]
    if li > lj:
        l[i] = lj
        l[j] = li
    #return l

def partition(l, lo, hi):
    
    l_len = l.shape[0]
    
    i = lo+1
    j = hi
    low = l[lo]
    #print(f'l: {l}, low: {low}, i {i}, l[i] {l[i]}, j: {j}, l[j] {l[j]}')
    
    #print(f'Partition - Lo: {lo}, hi: {hi}, i: {i}, j: {j}')
    while (j > i):
        #print(f'low: {low}, i {i}, l[i] {l[i]}, j: {j}, l[j] {l[j]}')
        while(i < hi and l[i] < low):
            i += 1

        while(j > lo and l[j] > low):
            j -= 1

        if i < j and i >= 0 and j <= hi:
            exch(l, i, j)

            if low == l[j] and low == l[i]:
                i += 1
        #print(f'After swap l: {l}')

    exch(l, lo, j)

    #print(f'Final swap l: {l}')

    return j

def sort(l, lo, hi):

    if hi == -1:
        hi = len(l) - 1
    
    if l.shape[0] > 1:
        j = partition(l, lo, hi)
        j_lo = j-1
        j_hi = j+1
        #print(l[lo:j_lo+1], l[j_hi:hi+1])
        if j_lo > lo:
            sort(l, lo, j_lo)
        if j_hi < hi:
            sort(l, j_hi, hi)

    return l

# Test
'''
arr = np.random.randint(0,10,10)
arr = np.array([5,9,1,8,7,0,3,6,2,4])
print('Partition 0')
j = partition(arr, 0, len(arr)-1)
print('Partition 1')
j_ = partition(arr, 0, j-1)
print('Partition 2')
j_ = partition(arr, j+1, len(arr)-1)
arr_sorted = sort(arr, 0, len(arr)-1)
assert is_sorted(arr_sorted)

'''

time_sort(sort, sort_kwargs={'lo':0, 'hi':-1}, duplicates=True, start=5, stop=13, tests=10)