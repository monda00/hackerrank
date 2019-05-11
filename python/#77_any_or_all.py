'''
Any or All
'''

if __name__ == '__main__':
    num = input()
    num_list = input().split()

    print(all([int(i) > 0 for i in num_list]) and any([j == j[::-1] for j in num_list]))

