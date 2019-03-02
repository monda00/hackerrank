'''
Validation phne number
'''

import re

if __name__ == '__main__':
    n = int(input())
    phone_number = []

    # input
    for i in range(n):
        phone_number.append(input())

    # pattern matching
    pattern = r"^[7|8|9]\d{9}"
    for i in range(n):
        match_number = re.fullmatch(pattern, str(phone_number[i]))
        if match_number != None:
            print("YES")
        else:
            print("NO")

