import numpy as np
import time

def merge(l1, l2):

    l1_len = l1.shape[0]
    l2_len = l2.shape[0]

    aux = np.zeros(l1_len+l2_len)

    l1_count = 0
    l2_count = 0
    aux_count = 0

    while aux_count < (l1_len + l2_len):#
        
        # If l1 is exhausted
        if l1_count == l1_len:
            #print(f'l1 exhausted')
            aux[aux_count] = l2[l2_count]
            l2_count += 1
        # If l2 is exhausted
        elif l2_count == l2_len:
            #print(f'l2 exhausted')
            aux[aux_count] = l1[l1_count]
            l1_count += 1

        elif l1_count < l1_len and l2_count < l2_len:
            if l1[l1_count] <= l2[l2_count]:
                aux[aux_count] = l1[l1_count]
                l1_count += 1
            else:
                aux[aux_count] = l2[l2_count]
                l2_count += 1

        aux_count += 1

    #print(f'Merging: l1: {l1}, l2: {l2}, output: {aux}')

    return aux




def split(l):

    split = int(l.shape[0]/2)
    l1 = l[:split]
    l2 = l[split:]
    assert l.shape[0] == (l1.shape[0]+l2.shape[0])
    
    return l1, l2

def sort(l):

    l1, l2 = split(l)

    if is_sorted(l1) == False:
        l1 = sort(l1)

    if is_sorted(l2) == False:
        l2 = sort(l2)

    return merge(l1, l2)

# Small test
arr = np.random.randint(0,100,11)
arr_sorted = sort(arr)
print(f'Arr: {arr}')
print(f'Arr sorted: {arr_sorted}')


