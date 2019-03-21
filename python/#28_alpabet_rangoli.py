'''
Alphabet Rangoli
'''

import string

def srange(n):
    return list(range(n))+list(range(n-2,-1,-1))

def print_rangoli(size):
    alpha = string.ascii_lowercase

    for i in srange(size):
        print('-'.join([alpha[size-j-1] for j in srange(i+1)]).center(4*(size-1)+1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

