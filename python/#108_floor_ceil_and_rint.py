'''
Floor, Ceil and Rint
'''

import numpy

if __name__ == '__main__':
    inp_arr = numpy.array(input().split(), float)
    numpy.set_printoptions(sign=' ')
    print(numpy.floor(inp_arr))
    print(numpy.ceil(inp_arr))
    print(numpy.rint(inp_arr))

