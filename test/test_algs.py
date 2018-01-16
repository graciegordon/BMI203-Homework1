import numpy as np
from BMI203-Homework1 import sorts

def test_empty_vector():
    #generate empty vector
    x=np.random.rand(0)
    
    #check bubblesort
    sortedX=np.sort(x)
    assert np.array_equal(sorts.bubble(x),sortedX)

    #check quicksort
    assert np.array_equal(sorts.quickSort(x),sortedX)

def test_signal_element_vector():
    #generate single element vector
    x=np.random.rand(1)

    #check bubblesort
    sortedX=np.sort(x)
    assert np.array_equal(sorts.bubble(x),sortedX)

    #check quicksort
    assert np.array_equal(sorts.quickSort(x),sortedX)

def duplicated_element_vector():
    temp= np.array([[1,2],[3,4]])
    x=np.repeat(temp, 2)

    sortedX=np.sort(x)

    #check bubblesort
    assert np.array_equal(sorts.bubble(x),sortedX)

    #check quicksort
    assert np.array_equal(sorts.quickSort(x),sortedX)

def test_varied_length_vector():
    x=np.random.rand(10)
    y=np.random.rand(11)

    sortedX=np.sort(x)
    sortedY=np.sort(y)

    #check bubblesort
    assert np.array_equal(sorts.bubble(x),sortedX)
    assert np.array_equal(sorts.bubble(y),sortedY)

    #check quicksort
    assert np.array_equal(sorts.quickSort(x),sortedX)
    assert np.array_equal(sorts.quickSort(y),sortedY)



