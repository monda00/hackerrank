'''
Exceptions
'''

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print("Error Code:", e)

