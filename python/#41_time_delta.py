'''
Time Delta
'''

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'

    first_time = datetime.strptime(t1, fmt)
    last_time = datetime.strptime(t2, fmt)
    delta = last_time - first_time
    return str(int(abs(delta.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

