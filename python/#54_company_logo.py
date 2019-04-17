'''
Company Logo
'''

import math
import os
import random
import re
import sys
from itertools import groupby

if __name__ == '__main__':
    print(*[c + " " + str(c_num) for c_num, c in sorted(len(list(v)), k)\
            for k, v in groupby(sorted(input()))], key=lambda x: (x[1], -x[0]))

