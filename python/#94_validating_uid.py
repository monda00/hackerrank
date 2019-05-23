'''
Validating UID
'''

import re

def is_valid(uid):
    uid = ''.join(sorted(uid))
    has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
    has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
    has_10_elements = bool(re.search(r'^[a-zA-Z0-9]{10}$', uid))
    no_repeats = not bool(re.search(r'(.)\1', uid))

    if has_2_or_more_upper and has_3_or_more_digits and has_10_elements\
            and no_repeats:
        return "Valid"
    else:
        return "Invalid"

if __name__ == '__main__':
    for _ in range(int(input())):
        print(is_valid(input()))

