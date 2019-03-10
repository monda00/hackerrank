'''
Concatenate
'''

import numpy as np

if __name__ == '__main__':
    n, m, p = map(int, input().split())

    array_1 = np.array([input().split() for _ in range(n)], int)
    array_2 = np.array([input().split() for _ in range(m)], int)

    print(np.concatenate((array_1, array_2), axis=0))

