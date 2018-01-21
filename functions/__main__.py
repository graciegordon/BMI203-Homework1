#run 

import numpy as np

from .sorts import quickSort, bubble

x = np.random.rand(10)
print("Unsorted input: ", x)
b1,bc,ba=bubble(x)
q1,qc,qa=quickSort(x,0,len(x)-1,0,0)
print("Bubble sort output: ", b1, bc, ba)
print("Quick sort output: ", q1,qc,qa)

#test time complexity

'''
def test_time(vectlen,num_iters):
    for i in range(0,num_iters):
        a=np.random.rand(vectlen)
        #test bubble
        bubble(a)
        #test quick
        quickSort(a,0,vectlen-1,0,0)

#test vector length 100
test_time(100, 100)
#test vector length 200
test_time(200, 100)
#test vector length 300
test_time(300, 100)
#test vector length 400
test_time(400, 100)
#test vector length 500
test_time(500, 100)
#test vector length 600
test_time(600, 100)
#test vector length 700
test_time(700, 100)
#test vector length 800
test_time(800, 100)
#test vector length 900
test_time(900, 100)
#test vector length 1000
test_time(1000, 100)
'''

    

