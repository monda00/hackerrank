'''
Nested Lists
'''
from operator import itemgetter

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    students.sort(key=itemgetter(1,0))
    second_score = sorted(list(set(score for name, score in students)))[1]

    for name, score in students:
        if score == second_score:
            print(name)

