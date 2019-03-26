'''
itertools.permutations()
'''

from itertools import permutations

if __name__ == '__main__':
    st, n = input().split()
    sorted_list = sorted(list(permutations(st, int(n))))

    print(*[''.join(c) for c in sorted_list], sep='\n')

