'''
Transpose and Flatten
'''

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    inp = []
    for _ in range(n):
        inp.append(input().split())

    inp_arr = numpy.array(inp, int)

    print(numpy.transpose(inp_arr))
    print(inp_arr.flatten())

