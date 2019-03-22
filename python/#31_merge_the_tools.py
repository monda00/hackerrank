'''
Merge the Tools!
'''

def merge_the_tools(string, k):
    for split_str in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in split_str if c not in d]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

