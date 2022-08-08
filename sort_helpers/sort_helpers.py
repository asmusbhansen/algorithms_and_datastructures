import numpy as np
import time
import matplotlib.pyplot as plt


# Timing test

def is_sorted(l):

    for i in range(l.shape[0]-1):
        if l[i] > l[i+1]:
            return False
    return True

def norm(arr):

    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

def time_sort(sort_func, sort_kwargs={}, duplicates=True, start=4, stop=14, tests=1000):
    
    
    N = np.array([2**n for n in np.arange(start, stop)])
    max_val = N[-1]
    results = np.zeros((tests, len(N)))

    for n, val in enumerate(N):
        
        for m in np.arange(tests):
            print(f'N = {val}, test = {m}')
            if duplicates:
                arr = np.random.randint(0,max_val, val)
            else:
                arr = np.arange(val)

            np.random.shuffle(arr)
            
            #print(f'arr: {arr}')
            time_start = time.time()
            arr_sorted = sort_func(arr, **sort_kwargs)
            
            results[m,n] = time.time() - time_start
            #print(f'arr_sorted: {arr_sorted}')
            assert (is_sorted(arr_sorted))
    
    t_mean = np.mean((results), axis=0)
    
    dN = np.diff(N)
    dt = np.diff(t_mean)
    
    #t_mean = np.log2(t_mean)
    #N = np.log2(N)
    
    t_mean = norm(t_mean)
    N = norm(N)

    plt.figure()
    plt.plot((N), (t_mean), '-o', label='Mean')
    #plt.xticks(np.log2(N), N)
    #plt.yticks(np.log2(np.mean(results, axis=0)), np.mean(results, axis=0))
    #plt.plot(N, np.percentile(results, q=10, axis=0), '-o', label='10th percentile')
    #plt.plot(N, np.percentile(results, q=90, axis=0), '-o', label='90th percentile')
    plt.legend()
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ylabel('Average run-time [s]')
    plt.xlabel('Array length')
    plt.gca().set_aspect('equal')
    
    plt.figure()
    plt.plot(dN, dt / dN, 'o')
    plt.xlabel('Delta N')
    plt.ylabel('Delta T / Delta N')
    plt.show()