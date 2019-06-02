'''
Min and Max
'''

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    inp_a = []
    for _ in range(n):
        inp_a.append(input().split())

    inp_arr = numpy.array(inp_a, int)

    min_arr = numpy.min(inp_arr, axis=1)
    print(numpy.max(min_arr))

