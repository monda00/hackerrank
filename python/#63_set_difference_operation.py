'''
Set.difference() Operation
'''

if __name__ == '__main__':
    e_num = int(input())
    e_student = set(input().split())
    f_num = int(input())
    f_student = set(input().split())

    print(len(e_student.difference(f_student)))

