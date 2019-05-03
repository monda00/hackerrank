'''
Check Strict Superset
'''

if __name__ == '__main__':
    a = set(input().split())
    flag = True
    for _ in range(int(input())):
        b = set(input().split())
        if not a.issuperset(b):
            print("False")
            exit()
    print("True")

