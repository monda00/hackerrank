'''
itertools.combinations_with_replacement()
'''

from itertools import combinations_with_replacement

if __name__ == '__main__':
    st, k = input().split()

    for co in combinations_with_replacement(sorted(st), int(k)):
        print(''.join(co))

