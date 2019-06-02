'''
Array Mathematics
'''

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    inp_a = []
    for _ in range(n):
        inp_a.append(input().split())

    a = numpy.array(inp_a, int)

    inp_b = []
    for _ in range(n):
        inp_b.append(input().split())

    b = numpy.array(inp_b, int)

    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))

