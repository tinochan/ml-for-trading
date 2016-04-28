"""Creating NumPy arrays."""
"""
http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html
http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html
"""

import numpy as np

def test_run():

    print 'List to 1D array'
    print np.array([2,3,4]) #[2,3,4]

    print 'List to 2D array'
    print np.array([(2,3,4),(5,6,7)]) #[[2,3,4][5 6 7]]

    print 'Empty array'
    print np.empty(5) #Floating values present in the corresponding memory location.
    print np.empty(5, dtype=np.int_) #Large random values

    print 'Array of 0s'
    print np.zeros(5) # 0. 0. 0. 0. 0.
    print np.zeros(5, dtype=np.int32) #0 0 0 0 0

    print 'Array of 1s'
    print np.ones((5,4)) #Show 1. as default is float
    print np.ones((5,4), dtype=np.int_) #Use dtype to defind the value as integer

    print 'Multidimensional arrays'
    print np.ndarray(shape=(3,2), dtype=float, order='F') #Row-major (C-style) or column-major (Fortran-style) order.
    print np.ndarray(shape=(3,2), dtype=float, order='C')

    print 'Generate an array full of random numbers, uniformly sampled from [0.0, 1.0)'
    print np.random.random((5,4)) #use tuple
    print np.random.rand(5,4) #not a tuple like mathlab syntax

    print 'Sample numbers from a Gaussian (normal) distribution'
    print np.random.normal(size=(2,3)) #Standard normal (mean = 0, s.d. =1)
    print np.random.normal(50, 10, size=(2,3)) #Change mean to 50 and s.d. to 10

    print 'Random integers'
    print np.random.randint(10) #a single integer in [0, 10)
    print np.random.randint(0, 10) #same as above, specifying [low, high) explicit
    print np.random.randint(0, 10, size=5) #5 random integers as a 1D array
    print np.random.randint(0, 10, size=(2,3)) #2x3 array of random integers

    print 'Array attributes'
    a = np.random.random((5,4)) #5x4 array of random numbers
    print a.shape #(5,4)
    print a.shape[0] #number of rows: 5
    print a.shape[1] #number of columns: 4
    print len(a.shape) #print the dimension of the array: 2
    print a.size #size of the array: 20
    print a.dtype #data type of the array: float64 (64bit floating point number)

if __name__ == "__main__":
    test_run()