'''
Check Subset
'''

if __name__ == '__main__':
    for _ in range(int(input())):
        a_num = input()
        a = set(input().split())
        b_num = input()
        b = set(input().split())
        print(a.issubset(b))

