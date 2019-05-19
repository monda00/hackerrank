'''
Hex Color Code
'''

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        matc = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})',
                          input())
        if matc:
            print(*matc, sep='\n')

