'''
The Captain's Room
'''

if __name__ == '__main__':
    k = int(input())
    room_number_list = list(map(int, input().split()))

    room_set = set(room_number_list)

    print(((sum(room_set)*k) - (sum(room_number_list))) // (k-1))

