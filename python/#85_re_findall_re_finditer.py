'''
Re.findall() & Re.finditer()
'''

import re

if __name__ == '__main__':
    vowels = 'aeiou'
    consonants = 'qwrtypsdfghjklzxcvbnm'
    mat = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants),
                     input(), flags=re.I)
    print('\n'.join(mat or ['-1']))

