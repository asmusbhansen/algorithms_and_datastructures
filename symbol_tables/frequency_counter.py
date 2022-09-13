from msilib.schema import Binary
from naive_st import NaiveSymbolTable
from binary_search_tree import BinarySearchTree
from LLRB_Tree import LLRBTree
import time
import matplotlib.pyplot as plt
import numpy as np
import random
from tqdm import tqdm

def switch_list(l, N):

    count = 0
    while count < N:

        idx1 = np.random.randint(0, len(l)-1)
        idx2 = np.random.randint(0, len(l)-1)
        if idx1 != idx2:
            count += 1
            l_temp = l[idx1]
            l[idx1] = l[idx2]
            l[idx2] = l_temp

    return l


def read_file(file_path):

    words = []

    # opening the text file
    with open(file_path,'r', encoding='utf8') as file:
    
        # reading each line    
        for line in file:
    
            # reading each word        
            for word in line.split():
                word = word.replace('.', '')
                words += [word] 

    return words

def frequency_counter(words, st=None):

    symbol_table = st()

    max_key = None
    max_val = 0

    for word in (words):

        if symbol_table.contains(word):
            val = symbol_table.get(word)+1
            symbol_table.put(word, val)
            
            if val > max_val:
                max_val = val
                max_key = word
            
        else:
            symbol_table.put(word, 1)

    '''
    # Find key with highest count
    max_word = ''
    symbol_table.put(max_word, 0)

    for key in tqdm(symbol_table.keys()):
        if symbol_table.get(key) > symbol_table.get(max_word):
            max_word = key
    '''
    #time_put = symbol_table.time_put
    #print(f'Max word: {max_key}, count: {max_val}')
    
    return symbol_table.depth()

file_location = r'C:\source/algorithms_and_datastructures/symbol_tables/'
file_path = 'leipzig1M.txt'
#file_path = 'simple_test.txt'
words = read_file(file_location + file_path)
words = [word for word in words if len(word) > 8]

#random.shuffle(words)
words.sort()

#words = switch_list(words, len(words)*0.33)

lens = []
ts = []
ts_bst = []
ds = []
ds_bst = []
downsample = [64, 32, 16]
tests = 10

for t in tqdm(np.arange(tests)):
    d = np.random.randint(50, 500)
    

    words = words[1:] + words[:1]

    words_downsample = words[:d]

    words_downsample_len = len(words_downsample)
    #print(f'Len words: {len(words_downsample)}')

    time_start = time.time()
    d = frequency_counter(words_downsample, st=LLRBTree)
    time_stop = time.time()
    ts += [(time_stop-time_start) * 1000 ]
    ds += [d]
    

    time_start = time.time()
    d = frequency_counter(words_downsample, st=BinarySearchTree)
    time_stop = time.time()
    ts_bst += [(time_stop-time_start) * 1000 ]
    ds_bst += [d]
    lens +=[words_downsample_len]

lens = np.array(lens)
ts = np.array(ts)
ts_bst = np.array(ts_bst)

#ts = (ts - np.percentile(ts, q=1)) / (np.percentile(ts, q=99) - np.percentile(ts, q=1))
#ts_bst = (ts_bst - np.percentile(ts_bst, q=1)) / (np.percentile(ts_bst, q=99) - np.percentile(ts_bst, q=1))

print(f'ts: {ts}')
print(f'ts_bst: {ts_bst}')

plt.figure()
plt.scatter(lens, ts, alpha=0.5, label='Left leaning Red-Black Tree')
plt.scatter(lens, ts_bst, alpha=0.5, label='Binary search tree')
plt.legend()
#plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Time')


plt.figure()
plt.scatter(lens, ds, alpha=0.5, label='Left leaning Red-Black Tree')
plt.scatter(lens, ds_bst, alpha=0.5, label='Binary search tree')
plt.legend()
#plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Depth')
plt.show()