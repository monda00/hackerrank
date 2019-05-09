'''
Any or All
'''

if __name__ == '__main__':
    num = int(input())
    num_list = list(map(int, input().split()))

    print(all([i > 0 for i in num_list]) and any([j == j[::-1] for j in num]))

