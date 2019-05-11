'''
ginortS
'''

if __name__ == '__main__':
    original_list = input()
    print(*(sorted(original_list, key=lambda x: (x.isdigit(),
                                                 x.isdigit() and int(x)%2==0,
                                                 x.isupper(),
                                                 x.islower(),
                                                 x))),sep='')

