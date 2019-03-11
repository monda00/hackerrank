'''
Lists
'''

if __name__ == '__main__':
    N = int(input())
    li = []

    for _ in range(N):
        inp = input().split()
        command = inp[0]
        if command == 'insert':
            li.insert(int(inp[1]), int(inp[2]))
        elif command == 'print':
            print(li)
        elif command == 'remove':
            li.remove(int(inp[1]))
        elif command == 'append':
            li.append(int(inp[1]))
        elif command == 'sort':
            li.sort()
        elif command == 'pop':
            li.pop()
        elif command == 'reverse':
            li.reverse()

