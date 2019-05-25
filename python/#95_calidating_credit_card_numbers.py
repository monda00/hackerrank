'''
Validating Credit Card Numbers
'''

import re

if __name__ == '__main__':
    valid_struc = r'[456]\d{3}(-?\d{4}){3}$'
    no_four_repeats = r'((\d)-?(?!(-?\2){3})){16}'

    for _ in range(int(input())):
        credit_card_number = input()
        if re.match(valid_struc, credit_card_number) and\
                re.match(no_four_repeats, credit_card_number):
            print("Valid")
        else:
            print("Invalid")

