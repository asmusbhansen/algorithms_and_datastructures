import numpy as np
from Heap import Heap
from tqdm import tqdm
import time
import matplotlib.pyplot as plt

class HeapSort(Heap):

    def is_sorted(self):
        
        arr = self.arr[1:]
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                print(f'i: {i}, i+1: {i+1}, arr[i]: {arr[i]}, arr[i+1]: {arr[i+1]}')
                print(f'self.arr: {self.arr}')
                return False
        return True

    def sort(self, arr):

        self.arr[1:] = arr
        self.size = len(arr)

        # Construct heap
        for i in range(self.size//2):
            i_ = self.size//2 - i
            #print(f'i_: {i_}')
            #print(f'arr: {self.arr}')
            self.sink(i_)
            #print(f'arr after sink: {self.arr}')
            

        #assert self.is_heap()

        # Sort
        count = 0
        while self.size > 1:
            #print(f'Iteration {count}, size: {self.size}')
            # First - Exchange first(largest) value with the last in the array and decrement size
            #print(f'Before exch: {self.arr}')
            self.exch(1, self.size)
            self.size -= 1
            # Second - Sink the first value into it's place
            #print(f'Before sink: {self.arr}')
            self.sink(1)
            #print(f'After sink: {self.arr}')
            count += 1
        
        #assert self.is_sorted()

        return self.arr[1:]
        
tests = 1000
max_heap_size = 1000

lens = []
ts = []

for t in tqdm(np.arange(tests)):
    N = np.random.randint(0,max_heap_size)
    lens += [N]
    arr_rand = np.random.randint(0, N, N)
    #print(f'arr_rand: {arr_rand}')
    hs = HeapSort(len(arr_rand))

    time_start = time.time()
    arr_sorted = hs.sort(arr_rand)
    ts += [time.time() - time_start]
    #print(f'arr_sorted: {arr_sorted}')

lens = np.array(lens)
ts = np.array(ts)

plt.figure()
plt.scatter(lens, ts, alpha=0.1)
plt.xlabel('N')
plt.ylabel('Time')
plt.show()