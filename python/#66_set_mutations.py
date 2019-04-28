'''
Set Mutations
'''

if __name__ == '__main__':
    n = int(input())
    set_num = set(map(int, input().split()))

    for _ in range(int(input())):
        command, *arg = input().split()
        getattr(set_num, command)(set(map(int, input().split())))

print(sum(set_num))

