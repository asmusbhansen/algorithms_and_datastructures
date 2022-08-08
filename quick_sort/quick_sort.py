import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, r'C:/source/algorithms_and_datastructures/sort_helpers') 
from sort_helpers import time_sort, is_sorted

# Set recursion limit
sys.setrecursionlimit(10**6)




# 3 partition implementation of quick sort

def exch(l, i, j):
    li = l[i]
    lj = l[j]
    #if li > lj:
    l[i] = lj
    l[j] = li
    #return l

def partition(l, lo, hi):
    
    l_len = l.shape[0]
    
    i = 0
    lt = 0
    gt = hi
 
    low = l[lo]
    
    while (gt >= i):
       
        #print(f'l: {l}, low: {low}, i {i}, l[i] {l[i]}, lt: {lt}, l[lt] {l[lt]}, gt: {gt}, l[gt] {l[gt]}')

        if i <= hi and l[i] < low:
            exch(l, lt, i)
            #print(f'Exch lt - i')
            lt += 1
            i += 1

        if i <= hi and l[i] > low:
            exch(l, gt, i)
            #print(f'Exch gt - i')
            gt -= 1

        if i <= hi and l[i] == low:
            i += 1
    #if hi-lo > 0:
    #    print(f'{(lt-lo)/(hi-lo):.3f}, {(gt-lo)/(hi-lo):.3f}')
    
    return lt, gt

def sort(l, lo, hi):

    if hi == -1:
        hi = len(l) - 1
    
    if l.shape[0] > 1:
        lt, gt = partition(l, lo, hi)
        
        if lt > lo:
            sort(l, lo, lt-1)
        if gt < hi:
            sort(l, gt+1, hi)

    return l

# Test

arr = np.random.randint(0,10,10)
arr = np.array([5,9,1,8,7,0,3,3,3,3,3,3,6,2,4])
#print('Partition 0')
#lt, gt = partition(arr, 0, len(arr)-1)
#print('Partition 1')
#lt_, gt_ = partition(arr, 0, lt-1)
#print('Partition 2')
#lt_, gt_ = partition(arr, gt+1, len(arr)-1)
arr_sorted = sort(arr, 0, len(arr)-1)
assert is_sorted(arr_sorted)

#plt.figure()
#plt.hist(lts, label='lts',alpha=0.5)
#plt.hist(gts, label='gts',alpha=0.5)
#plt.legend()

time_sort(sort, sort_kwargs={'lo':0, 'hi':-1}, duplicates=False, start=5, stop=12, tests=10)
