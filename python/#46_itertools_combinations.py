'''
itertools.combinations()
'''

from itertools import combinations

if __name__ == '__main__':
    st, k = input().split()

    for i in range(1, int(k)+1):
        for ch in combinations(sorted(st), i):
            print(''.join(ch))

