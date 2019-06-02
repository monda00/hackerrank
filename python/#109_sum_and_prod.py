'''
Sum and Prod
'''

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    inp_a = []
    for _ in range(n):
        inp_a.append(input().split())

    inp_arr = numpy.array(inp_a, int)

    sum_arr = numpy.sum(inp_arr, axis=0)
    print(numpy.prod(sum_arr))

