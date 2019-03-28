'''
DefaultDict Tutorial
'''

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)

    for i in range(n):
        d[input()].append(i+1)

    m_list = []
    for i in range(m):
        m_list.append(input())

    for i in m_list:
        if i in d:
            print(" ".join(map(str, d[i])))
        else:
            print(-1)

