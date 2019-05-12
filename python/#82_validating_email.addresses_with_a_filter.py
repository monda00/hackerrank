import re

def fun(s):
    # return True if s is a valid email, else return False
    return True if re.match(r"^[A-Za-z-_0-9]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$",s) else False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

