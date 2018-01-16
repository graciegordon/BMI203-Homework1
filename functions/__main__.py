#run 

import numpy as np

from sorts import bubble, quickSort

x = np.random.rand(10)
print("Unsorted input: ", x)

print("Bubble sort output: ", bubble(x))
print("Quick sort output: ", quicksort(x))
