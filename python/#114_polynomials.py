'''
Polynomials
'''

import numpy

if __name__ == '__main__':
    print(numpy.polyval(list(map(float, input().split())), float(input())))

