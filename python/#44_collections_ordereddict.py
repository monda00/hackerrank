'''
Collections.OrderedDict()
'''

from collections import OrderedDict

if __name__ == '__main__':
    items = OrderedDict()

    for _ in range(int(input())):
        item, space, price = input().rpartition(' ')
        items[item] = items.get(item, 0) + int(price)

    for item, price in items.items():
        print(item, price)

