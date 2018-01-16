#run 

import numpy as np

from .sorts import quickSort, bubble

x = np.random.rand(10)
print("Unsorted input: ", x)

print("Bubble sort output: ", bubble(x))
print("Quick sort output: ", quickSort(x,0,len(x)-1))
