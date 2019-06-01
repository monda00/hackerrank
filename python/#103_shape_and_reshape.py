'''
Shape and Reshape
'''

import numpy

if __name__ == '__main__':
    inp_arr = numpy.array(input().split(), int)
    print(numpy.reshape(inp_arr, (3, 3)))

