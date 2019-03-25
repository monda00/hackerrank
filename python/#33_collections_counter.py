'''
collections.Counter()
'''

from collections import Counter

if __name__ == '__main__':
    num_shoe = int(input())
    shoes = Counter(map(int, input().split()))
    num_cus = int(input())

    income = 0

    for i in range(num_cus):
        size, price = map(int, input().split())
        if shoes[size] != 0:
            income += price
            shoes[size] -= 1

    print(income)

