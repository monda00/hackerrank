'''
Eye and Identity
'''

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    numpy.set_printoptions(sign=' ')
    print(numpy.eye(n, m, k=0))

