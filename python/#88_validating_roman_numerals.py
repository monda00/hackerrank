'''
Validating Roman Numberals
'''

import re

if __name__ == '__main__':
    thousand = 'M{0,3}'
    hundered = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'
    regex_pattern = thousand + hundered + ten + digit + '$'
    print(str(bool(re.match(regex_pattern, input()))))

