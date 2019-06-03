'''
Linear Algebra
'''

import numpy

if __name__ == '__main__':
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], float)

    numpy.set_printoptions(legacy='1.13')
    print(numpy.linalg.det(a))

