'''
Group(), Groups() & Groupdict()
'''

import re

if __name__ == '__main__':
    mat = re.search(r'([a-zA-Z0-9])\1+', input())
    print(mat.group(1) if mat else -1)

