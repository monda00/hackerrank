'''
iterables ans iterators
'''

from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    st = input().split()
    k = int(input())

    conb = list(combinations(st, k))
    inc_a = [i for i in conb if 'a' in i]

    print(len(inc_a) / len(conb))

