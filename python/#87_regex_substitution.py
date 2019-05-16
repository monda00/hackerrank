'''
Regex Substitution
'''

import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )',
              lambda x: 'and' if x.group() == '&&' else 'or',
              input()))

