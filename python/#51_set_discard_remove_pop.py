'''
Set.discard(), remove() & .pop()
'''

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    for _ in range(int(input())):
        cmd, *num = input().split()
        if cmd == "pop":
            s.pop()
        elif cmd == "remove":
            s.remove(*map(int, num))
        elif cmd == "discard":
            s.discard(*map(int, num))

    print(sum(s))

