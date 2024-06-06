import numpy as np
from tqdm import tqdm
from Heap import Heap

class HeapPriorityQueue(Heap):


    def insert(self, num):
        insert_index = self.size+1
        #print(f'Inserting {num} at idx {insert_index}')
        self.arr[insert_index] = num
        self.swim(insert_index)
        #print(f'arr: {self.arr}')
        self.size += 1
        assert self.is_heap()

# Random test to ensure that heap is correctly implemented

tests = 10000
max_heap_size = 20
for t in tqdm(np.arange(tests)):
    N = np.random.randint(0,max_heap_size)
    
    hpq = HeapPriorityQueue(N)
    for i in range(N):
        rint = np.random.randint(0,100)

        hpq.insert(rint)
        assert hpq.is_heap()
    #print(f'hpq.arr: {hpq.arr}')
    last_removed = np.NaN
    while hpq.size > 0:
        remove_idx = 1
        remove_val = hpq.remove(remove_idx)
        if np.isfinite(last_removed) == False:
            last_removed = remove_val
        assert last_removed >= remove_val
        assert hpq.is_heap()
        last_removed = remove_val
'''
arr = np.array([97, 97, 86, 93, 54, 84, 71, 25, 59, 51, 53, 60, 60, 46, 49, 21, 25, 31, 34])
print(f'Arr: {arr}')
hpq = Heap(len(arr))
hpq.size = len(arr)
hpq.arr[1:] = arr     
last_removed = np.NaN  
while hpq.size > 0:
    remove_idx = 1
    remove_val = hpq.remove(remove_idx)
    print(f'Removed value: {remove_val}. Remaining: {hpq.arr}')
    if np.isfinite(last_removed) == False:
        last_removed = remove_val
    assert last_removed >= remove_val
    assert hpq.is_heap()
    last_removed = remove_val
'''