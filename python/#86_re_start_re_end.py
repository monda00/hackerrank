'''
Re.start() & Re.end()
'''

import re

if __name__ == '__main__':
    S = input()
    k = input()
    pattern = re.compile(k)
    search_res = pattern.search(S)

    if not search_res:
        print("(-1, -1)")
    while search_res:
        print("({0}, {1})".format(search_res.start(), search_res.end() - 1))
        search_res = pattern.search(S, search_res.start() + 1)

