"""Arithmetic operations."""

import numpy as np

def test_run():
    a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    print "Original array a:\n", a

    b = np.array([(100,200,300,400,500),(1,2,3,4,5)])
    print "Original array b:\n", b

    #Multiply a by 2
    print "\nDivide a by 2:\n", a*2

    #Divide a by 2
    print "\nDivide a by 2:\n", a/2

    #Divide a by 2.0
    print "\nDivide a by 2:\n", a/2.0

    #Multiply a and b (element wise)
    print "\nMultiply a and b:\n", a*b

    #Divide a and b (element wise)
    print "\nDivide a and b:\n", a/b

    #Dot product
    c = [[1, 0], [0, 1]]
    d = [[4, 1], [2, 2]]
    print "\nmatrix multiplication c and d:\n", np.dot(c,d)

if __name__ == "__main__":
    test_run()