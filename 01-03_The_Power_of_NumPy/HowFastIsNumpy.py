"""How fast is NumPy?"""

import numpy as np
from time import time

def how_long(func, *args):
    """Execute function with given arguments, and measure execution time."""
    t0 = time()
    result = func(*args) #all arguments are passed in as-is
    t1 = time()
    return result, t1 - t0

def manual_mean(arr):
    """Compute mean (average) of all elements in the given 2D array."""
    sum = 0
    for i in xrange(0, arr.shape[0]):
        for j in xrange (0, arr.shape[1]):
            sum = sum + arr[i, j]
    return sum / arr.size

def numpy_mean(arr):
    """Compute mean (average using NumPy."""
    return arr.mean()

def test_run():
    """Function called by Test Run."""
    nd1 = np.random.random((1000, 10000)) #use a sufficiently large array

    #Time the two functions, retrieving results and execution times
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print "Manual: {:.6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)".format(res_manual, t_manual, res_numpy, t_numpy)

    #Make sure both give us the same answer (upto some precision)
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

    #Compute speedup
    speedup = t_manual / t_numpy
    print "NumPy mean is", speedup, "times faster than manual for loops."

if __name__ == "__main__":
    test_run()