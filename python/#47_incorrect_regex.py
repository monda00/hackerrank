'''
Incorrect Regex
'''

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        ans = True
        try:
            reg = re.compile(input())
        except re.error:
            ans = False
        print(ans)

