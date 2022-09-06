from naive_st import NaiveSymbolTable
import time
import matplotlib.pyplot as plt
import numpy as np
import random

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

def frequency_counter(words, st=NaiveSymbolTable):

    symbol_table = st()

    for word in words:

        if symbol_table.contains(word):
            symbol_table.put(word, symbol_table.get(word)+1)
        else:
            symbol_table.put(word, 1)

    # Find key with highest count
    max_word = ''
    symbol_table.put(max_word, 0)

    for key in symbol_table.keys():
        if symbol_table.get(key) > symbol_table.get(max_word):
            max_word = key

    print(f'Max word: {max_word}, count: {symbol_table.get(max_word)}')

file_location = r'C:\source/algorithms_and_datastructures/symbol_tables/'
file_path = 'valiant_tailor.txt'
#file_path = 'simple_test.txt'
words = read_file(file_location + file_path)
random.shuffle(words)

lens = []
ts = []
downsample = [10, 8, 6, 4, 2, 1]
for d in downsample:
    
    time_start = time.time()
    frequency_counter(words[::d], st=NaiveSymbolTable)
    ts += [time.time() - time_start]
    lens +=[len(words[::d])]

lens = np.array(lens)
ts = np.array(ts)

plt.figure()
plt.scatter(lens, ts, alpha=1)
plt.xlabel('N')
plt.ylabel('Time')
plt.show()