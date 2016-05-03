"""Boolean or mask index arrays"""

import numpy as np

def test_run():
    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print a

    #calculating mean
    mean = a.mean()
    print mean

    #masking
    print a[a<mean]


if __name__ == "__main__":
    test_run()