'''
Text Wrap
'''

import textwrap

def wrap(string, max_width):
    wrap_list = textwrap.wrap(string, max_width)
    return '\n'.join(wrap_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

