'''
Validating and Parsing Email Addresses
'''

import email.utils
import re

if __name__ == '__main__':
    n = int(input())

    # input
    email_list = []
    for i in range(n):
        username, email = input().split()
        email_list.append({'username': username, 'email': email})

   # output
    pattern = r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
    for i in range(n):
        if(re.match(pattern, email_list[i]['email'])):
            print(email_list[i]['username'] + ' ' + email_list[i]['email'])

