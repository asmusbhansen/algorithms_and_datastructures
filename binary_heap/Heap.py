import numpy as np

class Heap:

    size = 0

    def __init__(self, N):

        self.arr = np.zeros(N+1) * np.NaN

    def remove(self, idx):
        val = self.arr[idx]
        self.exch(idx, self.size)
        self.arr[self.size] = np.NaN
        self.sink(idx)
        self.size -= 1
        return val

    def exch(self, i, j):
        i_temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = i_temp

    def less(self, i, j):
        return self.arr[i] < self.arr[j]

    def swim(self, k):

        while k > 1 and self.less(k//2, k):
            #print(f'idx {k//2} less than {k}, exch {self.arr[k//2]} and {self.arr[k]}')
            self.exch(k, k//2)
            k = k//2
            
    def sink(self, k):

        while 2*k <= self.size:
            
            j = 2*k

            # This introduces a bug - Should be implemented for non-binary Heap
            #while j+1 <=1 self.size and self.less(j, j+1):
            #    j += 1
            
            if j+1 <= self.size and self.less(j, j+1):
                j += 1

            # If the parent is not lesser than the children, break
            if self.less(k, j) == False:
                break
            else:
                self.exch(j,k)
                #print(f'Sink: exchange idx {j} and {k}. {self.arr[j]}, {self.arr[k]}')
                #print(f'Parent {self.arr[k]}')
  
            k = j


    def is_heap(self):
        '''
        if k*2 < self.size:
            
            if self.less(k, k*2) or self.less(k, k*2+1):
                return False

            return self.is_heap(k*2) and self.is_heap(k*2+1)

        else:
            return True
        '''
        for i in range(self.size):
            i_ = self.size - i
            if i_ > 1:

                if self.less(i_//2, i_):
                    print(f'Is heap?: {self.arr}')
                    print(f'Idx {i_//2} less than {i_}. {self.arr[i_//2]} less than {self.arr[i_]}')
                    return False
        return True
