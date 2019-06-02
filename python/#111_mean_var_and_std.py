'''
Mean, Var, and Std
'''

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    inp_a = []
    for _ in range(n):
        inp_a.append(input().split())

    inp_arr = numpy.array(inp_a, int)

    numpy.set_printoptions(legacy='1.13')
    print(numpy.mean(inp_arr, axis=1))
    print(numpy.var(inp_arr, axis=0))
    print(numpy.std(inp_arr))

