'''
Matrix Script
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    mat_t = ""
    for z in zip(*matrix):
        mat_t += "".join(z)

    print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", mat_t))

