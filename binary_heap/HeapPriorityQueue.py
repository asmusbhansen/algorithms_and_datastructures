import numpy as np
from tqdm import tqdm

class HeapPriorityQueue:

    size = 0

    def __init__(self, N):

        self.pq = np.zeros(N+1) * np.NaN

    def insert(self, num):
        insert_index = self.size+1
        #print(f'Inserting {num} at idx {insert_index}')
        self.pq[insert_index] = num
        self.swim(insert_index)
        #print(f'PQ: {self.pq}')
        self.size += 1

    def remove(self, idx):
        #print(f'Removing {self.pq[idx]} at idx {idx}')
        val = self.pq[idx]
        self.exch(idx, self.size)
        self.pq[self.size] = np.NaN
        self.sink(idx)
        #print(f'PQ: {self.pq}')
        self.size -= 1
        return val

    def exch(self, i, j):
        i_temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = i_temp

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def swim(self, k):

        while k > 1 and self.less(k//2, k):

            self.exch(k, k//2)
            k = k//2
            
    def sink(self, k):

        
        while 2*k < self.size:
            #print(f'k = {k}, val {self.pq[k]}. Children: {2*k} to {2*k+1} = {self.pq[2*k:2*k+1+1]}')
            j = 2*k
            while self.less(j, j+1) and j < 2*k+1:
                j += 1
            # If the parent is not lesser than the children, break
            if self.less(k, j) == False:
                break
            else:
                self.exch(j,k)
            k = j


    def is_heap(self, k=1):

        if k*2 < self.size:
            #print(f'k = {k}, value {self.pq[k]}, children: {self.pq[k*2]}, {self.pq[k*2+1]}')
            # If one of the children is larger than the parent
            if self.less(k, k*2) or self.less(k, k*2+1):
                return False

            return self.is_heap(k*2) and self.is_heap(k*2+1)

        else:
            return True

# Random test to ensure that heap is correctly implemented

tests = 1000
max_heap_size = 1000
for t in tqdm(np.arange(tests)):
    N = np.random.randint(0,max_heap_size)
    hpq = HeapPriorityQueue(N)
    for i in range(N):
        rint = np.random.randint(0,10)

        hpq.insert(rint)
        assert hpq.is_heap()

    last_removed = np.NaN
    while hpq.size > 0:
        remove_idx = 1
        remove_val = hpq.remove(remove_idx)
        if np.isfinite(last_removed) == False:
            last_removed = remove_val
        assert last_removed >= remove_val
        assert hpq.is_heap()
        last_removed = remove_val
         