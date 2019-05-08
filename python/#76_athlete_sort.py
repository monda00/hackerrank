'''
Athlete Sort
'''

from operator import itemgetter

if __name__ == '__main__':
    num_athlete, num_attr = map(int, input().split())

    athletes = []
    for _ in range(num_athlete):
        athletes.append(list(map(int, input().split())))

    for i in sorted(athletes, key=itemgetter(int(input()))):
        print(*i)

