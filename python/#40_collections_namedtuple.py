'''
Collections.namedtuple()
'''

from collections import namedtuple

if __name__ == '__main__':
    n, categories = (int(input()), input().split())
    Student = namedtuple('Student', categories)
    total = 0
    for _ in range(n):
        student = Student(*input().split())
        total += int(student.MARKS)
    print("{:.2f}".format(total/n))

