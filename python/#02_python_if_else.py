'''
Python If-Else
'''

if __name__ == '__main__':
    N = int(input())

    if N%2 == 1:
        print('Weird')
    elif N%2 == 0 and 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20:
        print('Weird')
    else:
        print('Not Weird')
