'''
Find the Runner-Up Score!
'''

if __name__ == '__main__':
    n = int(input())
    # set型にすることで重複を削除してくれる
    arr = list(set(map(int, input().split())))

    arr.sort(reverse=True)

    print(arr[1])

