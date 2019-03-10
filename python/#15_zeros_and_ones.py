'''
Zeros and Ones
'''

import numpy as np

if __name__ == '__main__':
    n, m, *p = map(int, input().split())

    print(np.zeros((n, m, *p), dtype=np.int))
    print(np.ones((n, m, *p), dtype=np.int))

