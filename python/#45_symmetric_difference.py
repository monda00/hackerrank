'''
Symmetric Difference
'''

if __name__ == '__main__':
    m_num = int(input())
    m = set(input().split())
    n_num = int(input())
    n = set(input().split())

    print('\n'.join(sorted(m^n, key=int)))

