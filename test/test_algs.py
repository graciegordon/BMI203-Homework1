import numpy as np
from functions import sorts

def test_empty_vector():
    #generate empty vector
    x=np.random.rand(0)
    
    #check bubblesort
    sortedX=np.sort(x)
    mysort,con,assign=sorts.bubble(x)
    assert np.array_equal(mysort,sortedX)
    
    #check quicksort
    mysort2,con2,assign2=sorts.quickSort(x, 0,len(x)-1,0,0)
    assert np.array_equal(mysort2,sortedX)

def test_signal_element_vector():
    #generate single element vector
    x=np.random.rand(1)
    
    sortedX=np.sort(x)
    mysort,con,assign=sorts.bubble(x)
    assert np.array_equal(mysort,sortedX)
    #check quicksort
    mysort2,con2,assign2=sorts.quickSort(x, 0,len(x)-1,0,0)
    assert np.array_equal(mysort2,sortedX)

def duplicated_element_vector():
    temp= np.array([[1,2],[3,4]])
    x=np.repeat(temp, 2)

    sortedX=np.sort(x)
    mysort,con,assign=sorts.bubble(x)
    assert np.array_equal(mysort,sortedX)
    
    #check quicksort
    mysort2,con2,assign2=sorts.quickSort(x, 0,len(x)-1,0,0)
    assert np.array_equal(mysort2,sortedX)

def test_varied_length_vector():
    x=np.random.rand(10)
    y=np.random.rand(11)

    sortedX=np.sort(x)
    mysort,con,assign=sorts.bubble(x)
    
    sortedY=np.sort(y)
    mysortY,conY,assignY=sorts.bubble(y)

    #check bubblesort
    
    
    assert np.array_equal(mysort,sortedX)
    assert np.array_equal(mysortY,sortedY)

    #check quicksort

    mysort2,con2,assign2=sorts.quickSort(x, 0,len(x)-1,0,0)
    mysort2y,con2y,assign2y=sorts.quickSort(y, 0,len(y)-1,0,0)
    
    assert np.array_equal(mysort2, sortedX)
    assert np.array_equal(mysort2y, sortedY)



